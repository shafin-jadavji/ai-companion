# Conventional Commit Message Guidelines

This project uses **Conventional Commits** to maintain clear and meaningful commit history.

## 📌 Format

```
<type>(optional scope): short, descriptive summary
```

### ✅ Example
```
feat(api): scaffold FastAPI with /ping and /chat endpoints
```

---

## 🔠 Allowed Commit Types

| Type       | Use For                                           |
|------------|--------------------------------------------------|
| `feat`     | A new feature or enhancement                     |
| `fix`      | A bug fix                                        |
| `docs`     | Documentation only changes                       |
| `style`    | Code style changes (e.g., formatting, spacing)   |
| `refactor` | Code changes that neither fix nor add features   |
| `test`     | Adding or modifying tests                        |
| `chore`    | Maintenance, build scripts, or tooling changes   |

---

## 🧠 Best Practices

- Use **imperative mood**: "add", not "added" or "adds"
- Keep the **summary under 72 characters**
- Optionally use a scope: `feat(chat)` or `fix(memory)`
- Include detailed explanation in the commit body if needed

---

## ✅ Good Commit Examples

- `feat(memory): add support for SQLite-based conversation history`
- `fix(api): resolve crash on empty chat input`
- `docs: add setup instructions to README`
- `chore: update dependencies and lock file`
