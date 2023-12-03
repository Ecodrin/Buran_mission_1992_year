import math
import time

import krpc

conn = krpc.connect(name='Buran Hohmann')
vessel = conn.space_center.active_vessel

ut = conn.add_stream(getattr, conn.space_center, 'ut')
altitude = conn.add_stream(getattr, vessel.flight(), 'mean_altitude')
apoapsis = conn.add_stream(getattr, vessel.orbit, 'apoapsis_altitude')
target = conn.space_center.target_vessel

vessel.auto_pilot.engage()
vessel.auto_pilot.target_direction = (0, 0, 1)

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

conn.space_center.rails_warp_factor = 6
close_enough = False
# # # КОСТЫЛИ
while abs(ang - required_angle) > 0.01:
    ang = target.flight(rf).longitude - vessel.flight(rf).longitude
    if not close_enough and abs(ang - required_angle) < (PI / 2 * rad2deg):
        conn.space_center.rails_warp_factor = 4
        close_enough = True
    if abs(ang - required_angle) < 3 and conn.space_center.rails_warp_factor > 0:
        conn.space_center.rails_warp_factor = 0
print('READY')
# # #




# Initial burn
delta_v1 = (mu / vessel.orbit.radius) ** 0.5 * (((2 * target.orbit.radius) / (target.orbit.radius + vessel.orbit.radius)) ** 0.5 - 1)

# Circularization burn
delta_v2 = (mu / target.orbit.radius) ** 0.5 * (1 - ((2 * vessel.orbit.radius) / (target.orbit.radius + vessel.orbit.radius)) ** 0.5)

node = vessel.control.add_node(ut() + abs(ang - required_angle) / vessel_ang_speed - abs(ang - required_angle) / target_ang_speed, prograde=delta_v1)


# Calculate burn time (using rocket equation)
F = vessel.available_thrust
Isp = vessel.specific_impulse * 9.82
m0 = vessel.mass
m1 = m0 / math.exp(delta_v1/Isp)
flow_rate = F / Isp / 4
burn_time = (m0 - m1) / flow_rate

# Orientate ship
vessel.auto_pilot.reference_frame = node.reference_frame
vessel.auto_pilot.target_direction = (0, 1, 0)
vessel.auto_pilot.wait()

vessel.control.throttle = 1

remaining_burn = conn.add_stream(node.remaining_burn_vector, node.reference_frame)
while remaining_burn()[1] > 1:
    pass
vessel.control.throttle = 0.0
node.remove()
