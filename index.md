# Портфолио
---
## Backend разработка

### Мобильное приложение TE-Manager

<div style="text-align: justify; margin-bottom: 25px;">
<b>С февраля 2024 года</b> в качестве фрилансера развиваю backend для мобильного приложения по управлению задачами и эмоциями. Наша команда <b>стала победителем гранта</b> размером в 1 млн рублей V очереди конкурса <b><a href="https://fasie.ru/upload/docs/Перечень%20победителей%20конкурса%20«Студенческий%20стартап»%20(очередь%20V).pdf" target="_blank">"Студенческий стартап"</a>.</b><br><br>

<b>Ключевые достижения:</b>
<ul style="margin:0 0 15px 24px; padding:0;">
    <li>
        <b>С нуля развернул production-сервер на Yandex Cloud:</b> установил и настроил <b>nginx</b>, обеспечил защищённое соединение по <b>HTTPS</b>, подключил домен и подготовил среду для масштабируемых веб-приложений.
    </li>
        <li>
        Реализовал <b>OpenAPI документацию</b> для удобного тестирования эндпоинтов через Swagger UI и быстрой проверки запросов.
    </li>
    <li>
        Использовал фреймворк <b>Flask (Python)</b> и базу данных <b>PostgreSQL</b>.
    </li>
    <li>
        Разработал <b>REST API</b> для приложения управления задачами с возможностью отслеживания времени, категоризации и приоритизации задач.
    </li>
    <li>
        Реализовал многоуровневую систему аутентификации с поддержкой <b>JWT-токенов</b> и OAuth-интеграцией с <b>Google</b> и <b>Яндекс</b>.
    </li>
    <li>
        Спроектировал и внедрил двустороннюю синхронизацию задач с <b>Яндекс.Календарём</b> (CalDAV).
    </li>
    <li>
        Создал модуль для отслеживания настроения пользователей с функциями анализа и визуализации данных.
    </li>
    <li>
        Разработал систему статистики для анализа продуктивности по категориям, важности и временным периодам.
    </li>
    <li>
        Интегрировал облачное хранилище <b>Yandex Object Storage</b> для пользовательских данных.
    </li>
    <li>
        Обеспечил безопасное хранение учётных данных и токенов с использованием современных методов шифрования.
    </li>
    <li>
        На старте проекта интегрировал решения в <b>Java Android приложение</b>.
    </li>
</ul>
<div style="margin-top:8px;">
    <b>Сайт проекта:</b> <a href="https://temanager.com" target="_blank" style="color:#0065a3; text-decoration:underline;">temanager.com</a>
</div>
</div>

<div style="margin-bottom: 40px; display: flex; justify-content: center;">
  <div style="box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 8px; overflow: hidden; width: 50%; max-width: 350px;">
    <img 
      src="https://i.postimg.cc/6qRZ03cN/Screenshot-4.png" 
      alt="Один из экранов приложения"
      style="display: block; width: 100%;"
    />
    <div style="background-color: #f8f8f8; padding: 10px; text-align: center;">
      <p style="margin: 0; font-style: italic; font-size: 14px;">Один из экранов приложения</p>
    </div>
  </div>
</div>

### Менеджер задач на Spring Boot

[![Static Badge](https://img.shields.io/badge/Open_on_GitHub-teal?logo=github)](https://github.com/casualdoto/java_task) <br>

<div style="text-align: justify; margin-bottom: 25px;">
  В учебных целях реализовал приложение - менеджер задач на Spring Boot.<br><br>

  <b>Ключевые технологии:</b>
  <ul style="margin:0 0 15px 24px; padding:0;">
    <li><b>Spring Boot 3.4</b> — основа приложения с поддержкой REST API</li>
    <li><b>Spring Data JPA</b> — доступ к данным через репозитории</li>
    <li><b>MariaDB</b> (production) + <b>Flyway</b> — миграции схемы</li>
    <li><b>Redis</b> — кэширование для прироста производительности</li>
    <li><b>Kafka</b> — асинхронная обработка событий (создание / просрочка задач)</li>
    <li><b>Docker &amp; Docker Compose</b> — контейнеризация приложения и инфраструктуры</li>
    <li><b>JUnit 5 &amp; Mockito</b> + <b>JaCoCo</b> — покрытие тестами &gt; 80 %</li>
  </ul>

  <b>Реализованная функциональность:</b>
  <ul style="margin:0 0 15px 24px; padding:0;">
    <li>Управление пользователями — регистрация и авторизация</li>
    <li><abbr title="Create / Read / Update / Delete">CRUD</abbr>-операции с задачами</li>
    <li>Система уведомлений о новых и просроченных задачах</li>
    <li>Асинхронный обмен сообщениями через <b>Kafka</b></li>
    <li>Кэширование данных в <b>Redis</b> (настраиваемый TTL)</li>
    <li>Профили окружения: <code>dev</code> / <code>prod</code></li>
    <li>Полная контейнеризация с многоконтейнерной архитектурой</li>
  </ul>

  <b>Архитектурные особенности:</b>
  <ul style="margin:0 0 15px 24px; padding:0;">
    <li>Многоуровневая структура: контроллеры → сервисы → репозитории</li>
    <li>Асинхронная обработка событий (Kafka + Scheduler для просроченных задач)</li>
    <li>Redis-кэширование с дифференцированным TTL</li>
    <li>Docker Compose — единая точка запуска всей экосистемы</li>
  </ul>

  <b>Достижения:</b>
  <ul style="margin:0 0 0 24px; padding:0;">
    <li>Покрытие кода тестами &gt; 80 %</li>
    <li>Реализована микросервисная (event-driven) архитектура</li>
    <li>Существенное сокращение времени отклика за счёт кэширования</li>
  </ul>

</div>

### Backend часть для ML-проекта

[![Static Badge](https://img.shields.io/badge/Open_on_GitHub-teal?logo=github)](https://github.com/casualdoto/labs_seminars_SPBSTU/tree/main) <br>

<div style="text-align: justify; margin-bottom: 25px;">
  <b>С декабря 2024 по март 2025 года</b> разрабатывался научно-исследовательский проект по предсказанию риска рака лёгких с применением машинного обучения. По итогам работы подготовлена научная статья, которая готовится к публикации в профильном журнале.<br><br>

  <b>Ключевые технологии:</b>
  <ul style="margin:0 0 15px 24px; padding:0;">
    <li><b>Python 3.9</b> — основной язык программирования</li>
    <li><b>Flask</b> — веб-фреймворк для создания REST API</li>
    <li><b>PostgreSQL</b> — реляционная СУБД для хранения пользовательских данных</li>
    <li><b>scikit-learn</b> — библиотека для построения и использования ML-моделей (SVM, KNN)</li>
    <li><b>Docker &amp; Docker Compose</b> — контейнеризация и автоматизация запуска сервисов</li>
  </ul>

  <b>Реализованный функционал:</b>
  <ul style="margin:0 0 15px 24px; padding:0;">
    <li>REST API для взаимодействия с фронтендом</li>
    <li>Эндпоинт <code>/predict</code> для приёма медицинских данных и возврата результатов</li>
    <li>Интеграция обученной <b>SVM-модели</b> для расчёта вероятности заболевания</li>
    <li>Сохранение истории прогнозов и пользовательских данных в <b>PostgreSQL</b></li>
  </ul>

  <b>Архитектурные решения:</b>
  <ul style="margin:0 0 15px 24px; padding:0;">
    <li>Микросервисная структура: фронтенд, бэкенд и база данных — как отдельные сервисы</li>
    <li>Автоматическая инициализация таблиц при запуске приложения</li>
    <li>Проверка доступности БД и настройка зависимостей между сервисами</li>
    <li>Контейнеризация всех компонентов для кроссплатформенного развёртывания</li>
  </ul>

  <b>Особенности реализации:</b>
  <ul style="margin:0 0 0 24px; padding:0;">
    <li>Предварительно обученная ML-модель (<b>SVM</b>) встроена в API</li>
    <li>Валидация и предварительная обработка входных данных</li>
    <li>Вывод вероятности риска в процентном выражении</li>
    <li>Хранение истории прогнозов для каждого пользователя</li>
  </ul>
</div>
## Аналитика данных в киберспорте

### Dota 2 Avulus

<div style="text-align: justify; margin-bottom: 25px;">
    <b>С октября 2024 года</b> работаю фриланс-аналитиком в профессиональной команде по Dota 2 — <b>Avulus</b>.
    <br><br>
    <b>Ключевые задачи:</b>
    <ul style="margin:0 0 10px 24px; padding:0;">
        <li>
            Сбор данных из открытых источников (<b>Spectral.gg</b>, <b>STRATZ</b>, <b>DotaBuff</b>, <b>OpenDota</b>, <b>Dota2ProTracker</b>).
        </li>
        <li>
            Извлечение инсайтов и подготовка аналитических отчётов для тренера и игроков.
        </li>
        <li>
            Автоматизация поиска информации и построение сервисов для команды (использую <b>Python</b> — <b>Pandas</b>, <b>NumPy</b>, <b>Matplotlib</b>, <b>MySQL</b>).
        </li>
        <li>
            Развёртывание собственного веб-сервиса на <b>Go</b> для автоматизированной аналитики и отчетов.
        </li>
        <li>
            Подготовка к соперникам: анализ паттернов, поиск закономерностей по оппонентам и их истории выступлений.
        </li>
        <li>
            Постоянная коммуникация с тренером и составом, предоставление данных по их запросам в удобном и наглядном виде.
        </li>
    </ul>
    <div style="margin-bottom:12px;"></div>

  <b>Достижения команды за время работы:</b>
  <ul style="margin:0 0 10px 24px; padding:0;">
      <li>1 место на <b>RES Regional Champions</b></li>
      <li>4 место на <b>CCT Series 5</b></li>
      <li>5–6 место на <b>ESL One Bangkok 2024</b></li>
      <li>7–8 место на <b>PGL Wallachia Season 2</b></li>
      <li>7–8 место на <b>ESL One Raleigh 2025</b></li>
  </ul>
  <div style="margin-bottom:12px;"></div>

  <b>Квалификации на крупнейшие турниры:</b>
  <ul style="margin:0 0 10px 24px; padding:0;">
      <li>1 место на <b>FISSURE PLAYGROUND #1: Western Europe Closed Qualifier</b></li>
      <li>1 место на <b>DreamLeague Season 25: Western Europe Closed Qualifier</b></li>
      <li>1 место на <b>PGL Wallachia Season 3: Western Europe Closed Qualifier</b></li>
      <li>2 место на <b>ESL One Bangkok 2024: Western Europe Closed Qualifier</b></li>
  </ul>
</div>


<h3 style="text-align: center; margin-bottom: 20px;">Примеры работ</h3>

<div style="margin-bottom: 40px; display: flex; justify-content: center;">
  <div style="box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 8px; overflow: hidden; max-width: 700px; width: 100%;">
    <img src="https://i.postimg.cc/wvVRyMnS/1stnight.png" style="display: block; width: 100%;"/>
    <div style="background-color: #f8f8f8; padding: 15px; text-align: center;">
      <p style="margin: 0; font-style: italic;">Карта распределения вардов за последние 8 матчей команды (на основе OpenDota API)</p>
    </div>
  </div>
</div>

<div style="margin-bottom: 40px; display: flex; justify-content: center;">
  <div style="box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 8px; overflow: hidden; max-width: 700px; width: 100%;">
    <img src="https://i.postimg.cc/rFpZptv2/Screenshot-3.png" style="display: block; width: 100%;"/>
    <div style="background-color: #f8f8f8; padding: 15px; text-align: center;">
      <p style="margin: 0; font-style: italic;">Пример автоматической генерации отчета по выбранным игрокам с моего сайта (количество матчей на герое за выбранное время и winrate (%))</p>
    </div>
  </div>
</div>

<div style="margin-bottom: 40px; display: flex; justify-content: center;">
  <div style="box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 8px; overflow: hidden; max-width: 700px; width: 100%;">
    <img src="https://i.postimg.cc/HWK22Prj/Screenshot-1.png" style="display: block; width: 100%;"/>
    <div style="background-color: #f8f8f8; padding: 15px; text-align: center;">
      <p style="margin: 0; font-style: italic;">Пример автоматической генерации отчета успешных героев против конкретного героя на выбранной позиции (1-5)</p>
    </div>
  </div>
</div>