### **README for USDC/AVAIL Dune Project**

---

#### **Project Overview**
This repository is designed to manage and automate SQL queries for the USDC/AVAIL pair on Uniswap using Dune Analytics. It includes scripts to pull, push, preview queries, and upload CSV data directly to Dune.

---

#### **Folder Structure**
```
usdc-avail-ak/
├── .env                   # Environment variables (e.g., DUNE_API_KEY)
├── queries.yml            # Query metadata (IDs and file paths)
├── queries/               # SQL queries
├── scripts/               # Python automation scripts
├── uploads/               # CSV files for Dune table uploads
└── requirements.txt       # Python dependencies
```

---

#### **Setup Guide**
1. **Clone the Repository**
   ```bash
   git clone https://github.com/AlwaysUbaid/usdc-avail-ak.git
   cd usdc-avail-ak
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add Your Dune API Key**
   - Create a `.env` file in the root directory:
     ```plaintext
     DUNE_API_KEY=your_dune_api_key
     ```

4. **Prepare Your Queries**
   - Add your SQL files in the `queries/` directory.
   - Update `queries.yml` with the corresponding query IDs and file paths.

---

#### **Scripts Usage**

1. **Pull Queries from Dune**
   - Download queries from Dune to your local `queries/` folder:
     ```bash
     python scripts/pull_from_dune.py
     ```

2. **Preview Query Results**
   - Preview the first 20 rows of a query:
     ```bash
     python scripts/preview_query.py <query_id>
     ```

3. **Push Queries to Dune**
   - Sync local queries to Dune:
     ```bash
     python scripts/push_to_dune.py
     ```

4. **Upload CSV Files**
   - Add CSV files to the `uploads/` folder and run:
     ```bash
     python scripts/upload_to_dune.py
     ```

---

#### **Notes**
- **Query IDs**: Ensure your query IDs in `queries.yml` match those on Dune.
- **CSV Uploads**: Only `.csv` files in the `uploads/` folder will be processed.

---

#### **Contributing**
Feel free to fork this repo and contribute improvements via pull requests.

---

#### **License**
This project is open-source and licensed under the MIT License.

---

You’re ready to manage and visualize your data with Dune Analytics! 🎉
