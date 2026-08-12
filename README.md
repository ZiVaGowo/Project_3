🤖 Automated Bug Investigator & PR Reviewer
Multi-Agent DevTools System based on LangGraph & Groq LLM

Автономная мультиагентная система для автоматического поиска, исправления багов в Python-коде и создания Pull Request'ов на GitHub.

📌 О проекте
Проект решает проблему рутинной отладки кода. Когда в системе происходит сбой, агент автоматически подтягивает упавший стек-трейс, находит проблемный файл в репозитории GitHub, генерирует исправление, проверяет его в изолированной песочнице и выкатывает готовый Pull Request.

🏗 Архитектура мультиагентной системы (LangGraph)
Система построена на базе паттерна Actor-Critic (Исполнитель — Критик) с циклом самоисправления (Self-Correction Loop):

## 🏗 Архитектура мультиагентной системы (LangGraph)

Система построена на базе паттерна **Actor-Critic (Исполнитель — Критик)** с циклом самоисправления (Self-Correction Loop). Оркестрация узлов выполняется с помощью LangGraph.

```mermaid
graph TD
    %% Стилевые классы
    classDef agent fill:#f9f,stroke:#333,stroke-width:2px,color:black;
    classDef decision fill:#fff9c4,stroke:#fbc02d,stroke-width:2px,color:black;

    %% Узлы и стартовые точки
    Start[📥 Вход: Stack Trace ошибки] --> Node1

    Node1("🔍 <b>1. Code Searcher Node</b><br/>(GitHub API)")
    Node2("⚡ <b>2. Code Fixer Node</b><br/>(Groq LLM)")
    Node3("🧪 <b>3. Test Sandbox Node</b><br/>(Код-песочница)")
    Decision{Проверка тестов}
    Node4("🚀 <b>4. PR Creator Node</b><br/>(GitHub API)")
    End[🎉 <b>Результат:</b> Готовый Pull Request]

    %% Применение стилей
    class Node1,Node2,Node3,Node4 agent;
    class Decision decision;

    %% Поток управления
    Node1 -->|Получен контекст кода| Node2
    Node2 -->|Сгенерировано исправление| Node3
    Node3 --> Decision
    
    Decision -->|✅ Успех| Node4
    Decision -->|❌ Ошибка| Node2
    
    Node4 --> End

    %% Стилизация стрелок (Успех / Ошибка)
    linkStyle 3 stroke:#4caf50,stroke-width:2px,color:#4caf50;
    linkStyle 4 stroke:#f44336,stroke-width:2px,color:#f44336;
