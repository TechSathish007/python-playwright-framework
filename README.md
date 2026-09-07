# 🎭 Next-Gen UI Automation with Playwright

A modern, lightning-fast web automation framework built with Python and Microsoft's Playwright. This project demonstrates Next-Gen UI testing capabilities, bypassing traditional web drivers for direct, high-speed browser manipulation.

## 🛠️ Tech Stack
- **Language:** Python 3.12
- **Core Engine:** Playwright (`pytest-playwright`)
- **Test Runner:** Pytest
- **Reporting:** Allure Reports
- **CI/CD:** GitHub Actions

## ⚙️ Core Architecture & Features
- **Auto-Waiting Engine:** Eliminates the need for explicit waits and `sleep()` commands by automatically waiting for UI elements to be actionable.
- **Codegen Integration:** Utilizes the Playwright Inspector to dynamically record user actions and generate production-ready automation scripts.
- **Headless Execution:** Blazing fast background execution optimized for cloud servers.
- **Cloud-Native CI/CD:** Fully automated YAML pipeline that downloads specialized Playwright browser binaries and executes the test suite on an Ubuntu server upon every code push.

## 🚀 How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/TechSathish007/python-playwright-framework.git](https://github.com/TechSathish007/python-playwright-framework.git)