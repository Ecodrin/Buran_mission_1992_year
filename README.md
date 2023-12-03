<!DOCTYPE html>
<html lang="ru">

<head>
  <meta charset="UTF-8">
</head>

<body>
  <font face="times new roman">
    <h1 align="center">Проект "Энергия - Буран, миссия 1992 года"</h1>
    <h3>команда CodeBrewers:</h3>
    <p>
        <li>Ecodrin - тимлид
        <li>Ke1thuzad - Программист
        <li>gakostennikov - Математик/физик
        <li>Liza2398 - Математик/физик
    </p>
    <h2 align="center">Немного истории:</h2>
    <p align="justify">Космический аппарат "Буран" был результатом амбициозного советского проекта,
    направленного на создание многоразового орбитального корабля. В этот день 1988 года "Буран"
    осуществил свой первый и единственный полет в рамках программы "Энергия-Буран". "Буран"
    был сопровождаемый ракетой-носителем "Энергия", которая вывела корабль на орбиту. После двух оборотов вокруг Земли, "Буран" успешно совершил автоматическую посадку. Программа "Энергия-Буран" стала одним из самых крупных и длительных проектов в истории советской космонавтики. В ее осуществлении приняло участие более 1200 организаций, включая
    предприятия, которые ныне входят в Ростех.
    "Буран" представлял собой значительный прорыв в развитии космической технологии и
    относился к семейству многоразовых орбитальных аппаратов.
    Согласно техническим заданиям Министерства обороны и отраслевым программам в НПО
    "Энергия" были разработаны технические предложения и
    эскизные проекты по решению конкретных задач в
    реальных направлениях применения ОК "Буран".
    Предусматривалось использовать ОК "Буран" для
    транспортно-технического обслуживания (ТТО) и
    ремонта орбитальных комплексов и космических
    аппаратов. Так, например, транспортно-техническое
    обслуживание орбитальным кораблем "Буран" комплекса
    "Мир" (на рисунке справа) - его дооснащение (доставка
    модулей,
    энергоустановок и др.), многоразовое использование модулей
    и оборудования (их возвращение для
    профилактики и ремонта), доставка на Землю
    результатов работ - позволяет существенно
    повысить эффективность комплекса. Как
    разновидности задачи ТТО были рассмотрены
    диагностирование неисправных аппаратов как на
    орбите, так и после их возвращения с помощью ОК
    "Буран", а также оценка возможности их ремонта и
    повторного использования. Применительно к
    аппаратам космической разведки исследована
    возможность возвращения двух неисправных аппаратов и принятия решений по их дальнейшему
    использованию.
    Детально проработано использование ОК "Буран" для развертывания и сборки больших
    конструкций. Это направление имеет принципиальное значение для создания космических
    антенн, солнечных энергоустановок и др. Обоснован эксперимент по отработке антенны
    космического радиотелескопа КРТ-30 и экспериментального космического комплекса
    наблюдения в составе бортового модуля на ОК "Буран". Особую роль ОК "Буран" может иметь
    для выведения и отработки на орбите особо дорогостоящих КА.
    </p>
    <h2 align="Center">Реализация миссии</h2>
    <ol>
        <li> Построение мат. модели.
        <li> KSP - постройка "Бурана".
        <li> autopilot
        <li> Сдача проекта.
    </ol>
    <h2 align="center">Реализазция в KSP</h2>
    <p>
        <ol>
            <li> Выход из атмосферы
            <img src="foto/KSP_x64 2023-12-02 17-37-02.jpg">
            <li> До отбрасывания ступеней
            <img src="foto/KSP_x64 2023-12-02 17-37-32.jpg">
            <img src="foto/KSP_x64 2023-12-02 17-41-13.jpg">
            <li> После отбрасывания ступеней
            <img src="foto/KSP_x64 2023-12-02 17-43-56.jpg">
            <img src="foto/KSP_x64 2023-12-02 17-45-19.jpg">
            <img src="foto/KSP_x64 2023-12-02 17-51-16.jpg">
        </ol>
    </p>
    <h3 align="center">Реализация автополота:</h3>
    Происходит в 2 этапа.
    <ol>
        <li>
            <p>
                <a href="buran_autopilot.py">Выход на орбиту ~150км</a>
                <br>
                Это облегчает программу и создает четкий план.
            </p>
        <li>
        <p>
                <a href="hohmann_auto.py">Выход на орбиту ~350км</a>
                <br>
                На этой орбите вращается орбитальная станция МИР.
                <br>
                Смена орбиты выполняется по Гомановской траектории.
            </p>
    </ol>
    <h3 align="center">Подсчет математической модели</h3>
    <p>
    Считается для сравнения результатов в KSP и подсчетов в матеметической модели.
    <a href="scripts.py">Файл</a>
    </p>
</font>
</body>

</html>