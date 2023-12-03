import krpc

conn = krpc.connect(name='Buran')
vessel = conn.space_center.active_vessel

ut = conn.add_stream(getattr, conn.space_center, 'ut')
altitude = conn.add_stream(getattr, vessel.flight(), 'mean_altitude')
apoapsis = conn.add_stream(getattr, vessel.orbit, 'apoapsis_altitude')
target = conn.space_center.target_vessel

PI = 3.141592653589793
rad2deg = 180 / PI
mu = vessel.orbit.body.gravitational_parameter

transfer_time = PI * (((target.orbit.radius + vessel.orbit.radius) ** 3) / (8 * mu)) ** 0.5

target_ang_speed = (mu / target.orbit.radius ** 3) ** 0.5
vessel_ang_speed = (mu / vessel.orbit.radius ** 3) ** 0.5

required_angle = (PI - target_ang_speed * transfer_time) * rad2deg

# Phase angle rate of change
phase_ang_RoC = abs(target_ang_speed - vessel_ang_speed)

rf = vessel.orbit.body.reference_frame
ang = target.flight(rf).longitude - vessel.flight(rf).longitude

# # # КОСТЫЛИ
while abs(ang - required_angle) > 0.01:
    ang = target.flight(rf).longitude - vessel.flight(rf).longitude
    if abs(ang - required_angle) < 3 and conn.space_center.rails_warp_factor > 0:
        conn.space_center.rails_warp_factor = 0
    print(ang)
conn.krpc.paused = True
print('READY')
# # #




# Initial burn
delta_v1 = (mu / vessel.orbit.radius) ** 0.5 * (((2 * target.orbit.radius) / (target.orbit.radius + vessel.orbit.radius)) ** 0.5 - 1)

# Circularization burn
delta_v2 = (mu / target.orbit.radius) ** 0.5 * (1 - ((2 * vessel.orbit.radius) / (target.orbit.radius + vessel.orbit.radius)) ** 0.5)

vessel.control.add_node(ut() + abs(ang - required_angle) / vessel_ang_speed - abs(ang - required_angle) / target_ang_speed, prograde=delta_v1)