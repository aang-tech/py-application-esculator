# Application Issue Esculator Tool

**Automated Diagnostic Data Collection for Application Support**

## 📖 The "Why"
In Application Support, the "Context Gap" is the time wasted between identifying a bug and giving a Developer enough information to fix it. This script eliminates the manual "grind" of checking versions, querying databases, and hunting for logs.

### The Problem
* **The Manual Grind:** 20+ minutes spent SSH-ing into servers and running manual SQL.
* **The Ping-Pong:** Developers asking follow-up questions because data was missing.
* **The Result:** High Mean Time to Resolution (MTTR) and engineer burnout.

### The Solution
A Python-based CLI tool that aggregates system metadata, database state, and log evidence into a single, developer-ready Markdown report in under **5 seconds**.

---

## 🛠 Features
- **Environment Metadata:** Auto-detects App Version, Server Node, and Environment Stage.
- **Database Snapshot:** Connects to PostgreSQL to pull user account status and flags.
- **Log Extraction:** (In Progress) Pulls relevant error traces based on timestamps.
- **Notification:** Formats everything into a clean Markdown report for instant escalation.

---

## 🏗 System Architecture

The script runs locally on the Support Engineer's machine, utilizing read-only access to remote environments to ensure production safety.

---

## 🚀 Getting Started

### 1. Installation
Clone the repository and install the required dependencies:
```bash
pip install psycopg2-binary python-dotenv
```
## Configuration
Create a .env file in the root directory:

```
DB_HOST=your-db-endpoint
DB_NAME=production_db
DB_USER=support_read_only
DB_PASS=your_secure_password
DB_PORT=5432
APP_ENV=Production
```

## Usage

```
python main.py --user-id <userid>
```

## Milestone
    [x] Setup files
    [x] Connect to endpoint
    [ ] View Log
    [ ] Connect to database
    [ ] Create report
    [ ] Send report to Slack with ticket info
