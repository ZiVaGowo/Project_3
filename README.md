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
    Start[📥 Вход: Stack Trace ошибки] --> Node1

    Node1["🔍 1. Code Searcher Node<br/>(GitHub API)"]
    Node2["⚡ 2. Code Fixer Node<br/>(Groq LLM)"]
    Node3["🧪 3. Test Sandbox Node<br/>(Код-песочница)"]
    Decision{"Проверка тестов"}
    Node4["🚀 4. PR Creator Node<br/>(GitHub API)"]
    End["🎉 Результат: Готовый Pull Request"]

    Node1 -->|Получен контекст кода| Node2
    Node2 -->|Сгенерировано исправление| Node3
    Node3 --> Decision
    
    Decision -->|Успех| Node4
    Decision -->|Ошибка| Node2
    
    Node4 --> End
