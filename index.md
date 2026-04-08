# <span class="lang-content lang-ru">Портфолио</span><span class="lang-content lang-en">Portfolio</span>
---
## <span class="lang-content lang-ru">Backend разработка</span><span class="lang-content lang-en">Backend Development</span>

### <span class="lang-content lang-ru">Go Currency Tracker</span><span class="lang-content lang-en">Go Currency Tracker</span>

[![Static Badge](https://img.shields.io/badge/Open_on_GitHub-teal?logo=github)](https://github.com/casualdoto/go-currency-tracker) <br>

<div class="lang-content lang-ru" style="text-align: justify; margin-bottom: 25px;">
  <b>В рамках практики в университете</b> разрабатывался проект по отслеживанию валютных курсов. По итогам работы создан полнофункциональный сервис для мониторинга курсов валют Центрального Банка России и криптовалют (Binance API) с веб-интерфейсом и Telegram ботом.<br><br>

  <b>Ключевые технологии:</b>
  <ul style="margin:0 0 15px 24px; padding:0;">
    <li><b>Go 1.23</b> — основной язык программирования для высокопроизводительных сервисов</li>
    <li><b>Chi Router</b> — HTTP роутер для создания REST API</li>
    <li><b>PostgreSQL</b> — реляционная СУБД для хранения исторических данных курсов валют</li>
    <li><b>Docker &amp; Docker Compose</b> — контейнеризация и автоматизация запуска микросервисов</li>
    <li><b>Telegram Bot API</b> — интеграция с мессенджером для уведомлений</li>
    <li><b>Binance API</b> — получение актуальных курсов криптовалют</li>
  </ul>

  <b>Реализованный функционал:</b>
  <ul style="margin:0 0 15px 24px; padding:0;">
    <li>REST API для взаимодействия с фронтендом и внешними системами</li>
    <li>Эндпоинты для получения курсов валют ЦБР с историческими данными</li>
    <li>Интеграция с Binance API для курсов криптовалют в рублях</li>
    <li>Веб-интерфейс с интерактивными графиками и экспортом в Excel</li>
    <li>Telegram бот с подписками на валюты и криптовалюты</li>
    <li>Автоматическое обновление курсов валют ежедневно в 23:59 UTC</li>
    <li>Мониторинг криптовалют каждые 15 минут с умными уведомлениями</li>
  </ul>

  <b>Архитектурные решения:</b>
  <ul style="margin:0 0 15px 24px; padding:0;">
    <li>Docker контейнеры: веб-сервер, Telegram бот и база данных</li>
    <li>Автоматическая инициализация таблиц при запуске приложения</li>
    <li>Проверка доступности БД и настройка зависимостей между сервисами</li>
    <li>Контейнеризация всех компонентов для кроссплатформенного развёртывания</li>
    <li>Graceful shutdown для корректного завершения работы сервисов</li>
  </ul>

  <b>Особенности реализации:</b>
  <ul style="margin:0 0 0 24px; padding:0;">
    <li>Хранение истории курсов валют и криптовалют с временными метками</li>
    <li>Система подписок пользователей на уведомления по конкретным валютам</li>
    <li>Экспорт исторических данных в Excel формат для анализа</li>
    <li>OpenAPI документация с Swagger UI для разработчиков</li>
  </ul>
</div>

<div class="lang-content lang-en" style="text-align: justify; margin-bottom: 25px;">
  <b>As part of university practice</b>, a project for tracking currency exchange rates was developed. As a result of the work, a fully functional service was created for monitoring Central Bank of Russia currency rates and cryptocurrencies (Binance API) with a web interface and Telegram bot.<br><br>

  <b>Key technologies:</b>
  <ul style="margin:0 0 15px 24px; padding:0;">
    <li><b>Go 1.23</b> — main programming language for high-performance services</li>
    <li><b>Chi Router</b> — HTTP router for creating REST API</li>
    <li><b>PostgreSQL</b> — relational DBMS for storing historical currency rate data</li>
    <li><b>Docker &amp; Docker Compose</b> — containerization and automation of microservice deployment</li>
    <li><b>Telegram Bot API</b> — integration with messenger for notifications</li>
    <li><b>Binance API</b> — obtaining current cryptocurrency rates</li>
  </ul>

  <b>Implemented functionality:</b>
  <ul style="margin:0 0 15px 24px; padding:0;">
    <li>REST API for interaction with frontend and external systems</li>
    <li>Endpoints for obtaining CBR currency rates with historical data</li>
    <li>Integration with Binance API for cryptocurrency rates in rubles</li>
    <li>Web interface with interactive charts and Excel export</li>
    <li>Telegram bot with subscriptions to currencies and cryptocurrencies</li>
    <li>Automatic currency rate updates daily at 23:59 UTC</li>
    <li>Cryptocurrency monitoring every 15 minutes with smart notifications</li>
  </ul>

  <b>Architectural solutions:</b>
  <ul style="margin:0 0 15px 24px; padding:0;">
    <li>Docker containers: web server, Telegram bot, and database</li>
    <li>Automatic table initialization when launching the application</li>
    <li>Database availability check and configuration of dependencies between services</li>
    <li>Containerization of all components for cross-platform deployment</li>
    <li>Graceful shutdown for proper service termination</li>
  </ul>

  <b>Implementation features:</b>
  <ul style="margin:0 0 0 24px; padding:0;">
    <li>Storage of currency and cryptocurrency rate history with timestamps</li>
    <li>User subscription system for notifications on specific currencies</li>
    <li>Export of historical data to Excel format for analysis</li>
    <li>OpenAPI documentation with Swagger UI for developers</li>
  </ul>
</div>

<div style="margin: 40px 0; display: flex; justify-content: center;">
  <div style="box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 8px; overflow: hidden; width: 90%; max-width: 950px;">
    <img 
      src="https://i.postimg.cc/LXNR2VSK/Screenshot-6.png" 
      alt="Экран анализа валютных курсов"
      style="display: block; width: 100%;"
    />
    <div style="background-color: #f8f8f8; padding: 10px; text-align: center;">
      <p class="lang-content lang-ru" style="margin: 0; font-style: italic; font-size: 14px;">
        Экран анализа валютных курсов в приложении
      </p>
      <p class="lang-content lang-en" style="margin: 0; font-style: italic; font-size: 14px;">
        Currency rate analysis screen in the app
      </p>
    </div>
  </div>
</div>

<div style="margin: 40px 0; display: flex; justify-content: center;">
  <div style="box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 8px; overflow: hidden; width: 90%; max-width: 950px;">
    <img 
      src="https://i.postimg.cc/k5qkGtfn/Screenshot-7.png" 
      alt="Экран анализа валютных курсов"
      style="display: block; width: 100%;"
    />
    <div style="background-color: #f8f8f8; padding: 10px; text-align: center;">
      <p class="lang-content lang-ru" style="margin: 0; font-style: italic; font-size: 14px;">
        Экран анализа криптовалютных курсов в приложении
      </p>
      <p class="lang-content lang-en" style="margin: 0; font-style: italic; font-size: 14px;">
        Cryptocurrency rate analysis screen in the app
      </p>
    </div>
  </div>
</div>

<div style="margin: 40px 0; display: flex; justify-content: center;">
  <div style="box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 8px; overflow: hidden; width: 60%; max-width: 400px;">
    <img 
      src="https://i.postimg.cc/mgsb3k8n/Screenshot-8.png" 
      alt="Пример работы Telegram-бота"
      style="display: block; width: 100%;"
    />
    <div style="background-color: #f8f8f8; padding: 10px; text-align: center;">
      <p class="lang-content lang-ru" style="margin: 0; font-style: italic; font-size: 14px;">
        Пример работы Telegram-бота: обновления валют и криптовалют
      </p>
      <p class="lang-content lang-en" style="margin: 0; font-style: italic; font-size: 14px;">
        Example of Telegram bot in action: currency and crypto updates
      </p>
    </div>
  </div>
</div>

### <span class="lang-content lang-ru">Мобильное приложение TE-Manager</span><span class="lang-content lang-en">TE-Manager Mobile App</span>

<div class="lang-content lang-ru" style="text-align: justify; margin-bottom: 25px;">
<b>С марта 2024 года</b> в качестве фрилансера развиваю backend для мобильного приложения по управлению задачами и эмоциями. Наша команда <b>стала победителем гранта</b> размером в 1 млн рублей V очереди конкурса <b><a href="https://fasie.ru/upload/docs/Перечень%20победителей%20конкурса%20«Студенческий%20стартап»%20(очередь%20V).pdf" target="_blank">"Студенческий стартап"</a>.</b><br><br>

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

<b>Техническое развитие и модернизация:</b>
<ul style="margin:0 0 15px 24px; padding:0;">
    <li>
        <b>Микросервисная архитектура:</b> Переписал монолитное Flask-приложение на микросервисную архитектуру с использованием <b>FastAPI (Python)</b> и <b>Go-сервиса</b> для лучшей производительности. Внедрил Docker-контейнеризацию для упрощения развертывания и масштабирования. Реализовал взаимодействие между сервисами через HTTP API с валидацией данных.
    </li>
    <li>
        <b>Модернизация безопасности:</b> Полностью обновил JWT-систему: заменил HS256 на RS256 (асимметричная криптография). Внедрил систему отзыва токенов (blacklist) с возможностью принудительного выхода со всех устройств. Добавил device fingerprinting для привязки токенов к устройствам. Реализовал каскадный отзыв токенов при обнаружении компрометации.
    </li>
    <li>
        <b>Система аутентификации без паролей:</b> Заменил традиционную аутентификацию на систему кодов верификации через email/SMS. Интегрировал Redis для кэширования кодов и rate limiting.
    </li>
    <li>
        <b>Технические улучшения:</b> Внедрил версионирование API. Добавил comprehensive health checks для всех сервисов. Реализовал детальное логирование и мониторинг производительности. Создал систему фоновых задач для автоматической очистки устаревших данных.
    </li>
    <li>
        <b>Инфраструктура:</b> Настроил nginx с улучшенной конфигурацией для микросервисов. Интегрировал Redis для кэширования и управления состоянием. Создал Docker Compose конфигурацию для локальной разработки и тестирования.
    </li>
</ul>

<div style="margin-top:8px;">
    <b>Сайт проекта:</b> <a href="https://temanager.com" target="_blank" style="color:#0065a3; text-decoration:underline;">temanager.com</a>
</div>
</div>

<div class="lang-content lang-en" style="text-align: justify; margin-bottom: 25px;">
<b>Since March 2024</b>, I have been working as a freelancer developing the backend for a mobile application for task and emotion management. Our team <b>won a grant</b> of 1 million rubles in the V round of the <b><a href="https://fasie.ru/upload/docs/Перечень%20победителей%20конкурса%20«Студенческий%20стартап»%20(очередь%20V).pdf" target="_blank">"Student Startup"</a> competition.</b><br><br>

<b>Key achievements:</b>
<ul style="margin:0 0 15px 24px; padding:0;">
    <li>
        <b>Built a production server from scratch on Yandex Cloud:</b> installed and configured <b>nginx</b>, ensured secure <b>HTTPS</b> connection, connected a domain, and prepared an environment for scalable web applications.
    </li>
        <li>
        Implemented <b>OpenAPI documentation</b> for convenient endpoint testing via Swagger UI and quick request verification.
    </li>
    <li>
        Used the <b>Flask (Python)</b> framework and <b>PostgreSQL</b> database.
    </li>
    <li>
        Developed a <b>REST API</b> for a task management application with time tracking, categorization, and task prioritization capabilities.
    </li>
    <li>
        Implemented a multi-level authentication system with <b>JWT token</b> support and OAuth integration with <b>Google</b> and <b>Yandex</b>.
    </li>
    <li>
        Designed and implemented two-way task synchronization with <b>Yandex.Calendar</b> (CalDAV).
    </li>
    <li>
        Created a module for tracking user moods with data analysis and visualization functions.
    </li>
    <li>
        Developed a statistics system for analyzing productivity by categories, importance, and time periods.
    </li>
    <li>
        Integrated <b>Yandex Object Storage</b> cloud storage for user data.
    </li>
    <li>
        Ensured secure storage of credentials and tokens using modern encryption methods.
    </li>
    <li>
        Integrated solutions into a <b>Java Android application</b> at the start of the project.
    </li>
</ul>

<b>Technical Development and Modernization:</b>
<ul style="margin:0 0 15px 24px; padding:0;">
    <li>
        <b>Microservice Architecture:</b> Rewrote the monolithic Flask application to a microservice architecture using <b>FastAPI (Python)</b> and <b>Go service</b> for better performance. Implemented Docker containerization for simplified deployment and scaling. Realized inter-service communication through HTTP API with data validation.
    </li>
    <li>
        <b>Security Modernization:</b> Completely updated the JWT system: replaced HS256 with RS256 (asymmetric cryptography). Implemented a token revocation system (blacklist) with the ability to force logout from all devices. Added device fingerprinting for token binding to devices. Implemented cascading token revocation upon compromise detection.
    </li>
    <li>
        <b>Passwordless Authentication System:</b> Replaced traditional authentication with a verification code system via email/SMS. Integrated Redis for code caching and rate limiting. 
    </li>
    <li>
        <b>Technical Improvements:</b> Implemented API versioning. Added comprehensive health checks for all services. Implemented detailed logging and performance monitoring. Created a background task system for automatic cleanup of outdated data.
    </li>
    <li>
        <b>Infrastructure:</b> Configured nginx with improved configuration for microservices. Integrated Redis for caching and state management. Created Docker Compose configuration for local development and testing.
    </li>
</ul>

<div style="margin-top:8px;">
    <b>Project website:</b> <a href="https://temanager.com" target="_blank" style="color:#0065a3; text-decoration:underline;">temanager.com</a>
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
      <p class="lang-content lang-ru" style="margin: 0; font-style: italic; font-size: 14px;">Один из экранов приложения</p>
      <p class="lang-content lang-en" style="margin: 0; font-style: italic; font-size: 14px;">One of the app screens</p>
    </div>
  </div>
</div>

### <span class="lang-content lang-ru">Менеджер задач на Spring Boot</span><span class="lang-content lang-en">Task Manager on Spring Boot</span>

[![Static Badge](https://img.shields.io/badge/Open_on_GitHub-teal?logo=github)](https://github.com/casualdoto/java_task) <br>

<div class="lang-content lang-ru" style="text-align: justify; margin-bottom: 25px;">
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

<div class="lang-content lang-en" style="text-align: justify; margin-bottom: 25px;">
  For educational purposes, I implemented a task manager application using Spring Boot.<br><br>

  <b>Key technologies:</b>
  <ul style="margin:0 0 15px 24px; padding:0;">
    <li><b>Spring Boot 3.4</b> — application foundation with REST API support</li>
    <li><b>Spring Data JPA</b> — data access through repositories</li>
    <li><b>MariaDB</b> (production) + <b>Flyway</b> — schema migrations</li>
    <li><b>Redis</b> — caching for performance improvement</li>
    <li><b>Kafka</b> — asynchronous event processing (task creation / expiration)</li>
    <li><b>Docker &amp; Docker Compose</b> — containerization of application and infrastructure</li>
    <li><b>JUnit 5 &amp; Mockito</b> + <b>JaCoCo</b> — test coverage &gt; 80 %</li>
  </ul>

  <b>Implemented functionality:</b>
  <ul style="margin:0 0 15px 24px; padding:0;">
    <li>User management — registration and authorization</li>
    <li><abbr title="Create / Read / Update / Delete">CRUD</abbr> operations with tasks</li>
    <li>Notification system for new and overdue tasks</li>
    <li>Asynchronous message exchange via <b>Kafka</b></li>
    <li>Data caching in <b>Redis</b> (configurable TTL)</li>
    <li>Environment profiles: <code>dev</code> / <code>prod</code></li>
    <li>Full containerization with multi-container architecture</li>
  </ul>

  <b>Architectural features:</b>
  <ul style="margin:0 0 15px 24px; padding:0;">
    <li>Multi-layer structure: controllers → services → repositories</li>
    <li>Asynchronous event processing (Kafka + Scheduler for overdue tasks)</li>
    <li>Redis caching with differentiated TTL</li>
    <li>Docker Compose — single launch point for the entire ecosystem</li>
  </ul>

  <b>Achievements:</b>
  <ul style="margin:0 0 0 24px; padding:0;">
    <li>Code test coverage &gt; 80 %</li>
    <li>Implemented microservice (event-driven) architecture</li>
    <li>Significant response time reduction through caching</li>
  </ul>

</div>

### <span class="lang-content lang-ru">Backend часть для ML-проекта</span><span class="lang-content lang-en">Backend for ML Project</span>

[![Static Badge](https://img.shields.io/badge/Open_on_GitHub-teal?logo=github)](https://github.com/casualdoto/labs_seminars_SPBSTU/tree/main) <br>

<div class="lang-content lang-ru" style="text-align: justify; margin-bottom: 25px;">
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

<div class="lang-content lang-en" style="text-align: justify; margin-bottom: 25px;">
  <b>From December 2024 to March 2025</b>, a research project was developed to predict lung cancer risk using machine learning. As a result of the work, a scientific article has been prepared and is being prepared for publication in a specialized journal.<br><br>

  <b>Key technologies:</b>
  <ul style="margin:0 0 15px 24px; padding:0;">
    <li><b>Python 3.9</b> — main programming language</li>
    <li><b>Flask</b> — web framework for creating REST API</li>
    <li><b>PostgreSQL</b> — relational DBMS for storing user data</li>
    <li><b>scikit-learn</b> — library for building and using ML models (SVM, KNN)</li>
    <li><b>Docker &amp; Docker Compose</b> — containerization and service launch automation</li>
  </ul>

  <b>Implemented functionality:</b>
  <ul style="margin:0 0 15px 24px; padding:0;">
    <li>REST API for interaction with the frontend</li>
    <li><code>/predict</code> endpoint for receiving medical data and returning results</li>
    <li>Integration of a trained <b>SVM model</b> for calculating disease probability</li>
    <li>Saving prediction history and user data in <b>PostgreSQL</b></li>
  </ul>

  <b>Architectural solutions:</b>
  <ul style="margin:0 0 15px 24px; padding:0;">
    <li>Microservice structure: frontend, backend, and database as separate services</li>
    <li>Automatic table initialization when launching the application</li>
    <li>Database availability check and configuration of dependencies between services</li>
    <li>Containerization of all components for cross-platform deployment</li>
  </ul>

  <b>Implementation features:</b>
  <ul style="margin:0 0 0 24px; padding:0;">
    <li>Pre-trained ML model (<b>SVM</b>) embedded in API</li>
    <li>Validation and preprocessing of input data</li>
    <li>Output of risk probability as a percentage</li>
    <li>Storage of prediction history for each user</li>
  </ul>
</div>

## <span class="lang-content lang-ru">Аналитика данных в киберспорте</span><span class="lang-content lang-en">Data Analytics in Esports</span>

### Dota 2 Avulus

<div class="lang-content lang-ru" style="text-align: justify; margin-bottom: 25px;">
    <b>С октября 2024 года по апрель 2026</b> работал фриланс-аналитиком в профессиональной команде по Dota 2 — <b>Avulus</b>.
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

<div class="lang-content lang-en" style="text-align: justify; margin-bottom: 25px;">
    <b>From October 2024 to April 2026</b>, I have been working as a freelance analyst for the professional Dota 2 team — <b>Avulus</b>.
    <br><br>
    <b>Key tasks:</b>
    <ul style="margin:0 0 10px 24px; padding:0;">
        <li>
            Data collection from open sources (<b>Spectral.gg</b>, <b>STRATZ</b>, <b>DotaBuff</b>, <b>OpenDota</b>, <b>Dota2ProTracker</b>).
        </li>
        <li>
            Extracting insights and preparing analytical reports for the coach and players.
        </li>
        <li>
            Automating information search and building services for the team (using <b>Python</b> — <b>Pandas</b>, <b>NumPy</b>, <b>Matplotlib</b>, <b>MySQL</b>).
        </li>
        <li>
            Deploying a custom web service on <b>Go</b> for automated analytics and reports.
        </li>
        <li>
            Preparation for opponents: pattern analysis, finding regularities in opponents and their performance history.
        </li>
        <li>
            Constant communication with the coach and team, providing data according to their requests in a convenient and visual format.
        </li>
    </ul>
    <div style="margin-bottom:12px;"></div>

  <b>Team achievements during my work:</b>
  <ul style="margin:0 0 10px 24px; padding:0;">
      <li>1st place at <b>RES Regional Champions</b></li>
      <li>4th place at <b>CCT Series 5</b></li>
      <li>5–6th place at <b>ESL One Bangkok 2024</b></li>
      <li>7–8th place at <b>PGL Wallachia Season 2</b></li>
      <li>7–8th place at <b>ESL One Raleigh 2025</b></li>
  </ul>
  <div style="margin-bottom:12px;"></div>

  <b>Qualifications for major tournaments:</b>
  <ul style="margin:0 0 10px 24px; padding:0;">
      <li>1st place at <b>FISSURE PLAYGROUND #1: Western Europe Closed Qualifier</b></li>
      <li>1st place at <b>DreamLeague Season 25: Western Europe Closed Qualifier</b></li>
      <li>1st place at <b>PGL Wallachia Season 3: Western Europe Closed Qualifier</b></li>
      <li>2nd place at <b>ESL One Bangkok 2024: Western Europe Closed Qualifier</b></li>
  </ul>
</div>


<h3 style="text-align: center; margin-bottom: 20px;">
  <span class="lang-content lang-ru">Примеры работ</span>
  <span class="lang-content lang-en">Work Examples</span>
</h3>

<div style="margin-bottom: 40px; display: flex; justify-content: center;">
  <div style="box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 8px; overflow: hidden; max-width: 700px; width: 100%;">
    <img src="https://i.postimg.cc/wvVRyMnS/1stnight.png" style="display: block; width: 100%;"/>
    <div style="background-color: #f8f8f8; padding: 15px; text-align: center;">
      <p class="lang-content lang-ru" style="margin: 0; font-style: italic;">Карта распределения вардов за последние 8 матчей команды (на основе OpenDota API)</p>
      <p class="lang-content lang-en" style="margin: 0; font-style: italic;">Ward distribution map for the team's last 8 matches (based on OpenDota API)</p>
    </div>
  </div>
</div>

<div style="margin-bottom: 40px; display: flex; justify-content: center;">
  <div style="box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 8px; overflow: hidden; max-width: 700px; width: 100%;">
    <img src="https://i.postimg.cc/rFpZptv2/Screenshot-3.png" style="display: block; width: 100%;"/>
    <div style="background-color: #f8f8f8; padding: 15px; text-align: center;">
      <p class="lang-content lang-ru" style="margin: 0; font-style: italic;">Пример автоматической генерации отчета по выбранным игрокам с моего сайта (количество матчей на герое за выбранное время и winrate (%))</p>
      <p class="lang-content lang-en" style="margin: 0; font-style: italic;">Example of automatic report generation for selected players from my website (number of matches on a hero for the selected time and winrate (%))</p>
    </div>
  </div>
</div>

<div style="margin-bottom: 40px; display: flex; justify-content: center;">
  <div style="box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 8px; overflow: hidden; max-width: 700px; width: 100%;">
    <img src="https://i.postimg.cc/HWK22Prj/Screenshot-1.png" style="display: block; width: 100%;"/>
    <div style="background-color: #f8f8f8; padding: 15px; text-align: center;">
      <p class="lang-content lang-ru" style="margin: 0; font-style: italic;">Пример автоматической генерации отчета успешных героев против конкретного героя на выбранной позиции (1-5)</p>
      <p class="lang-content lang-en" style="margin: 0; font-style: italic;">Example of automatic report generation of successful heroes against a specific hero in the selected position (1-5)</p>
    </div>
  </div>
</div>