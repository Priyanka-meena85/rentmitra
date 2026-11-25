const fs = require('node:fs');
const path = require('node:path');

const DB_PATH = path.join(__dirname, '..', 'data', 'db.json');

class Database {
  static get() {
    try {
      const data = fs.readFileSync(DB_PATH, 'utf-8');
      return JSON.parse(data);
    } catch (err) {
      console.error('Failed to read db.json:', err.message);
      return {
        properties: [],
        tenants: [],
        rentCollections: [],
        commissions: [],
        leads: [],
        complaints: []
      };
    }
  }

  static save(data) {
    try {
      fs.writeFileSync(DB_PATH, JSON.stringify(data, null, 2), 'utf-8');
      return true;
    } catch (err) {
      console.error('Failed to write db.json:', err.message);
      return false;
    }
  }

  static getCollection(collectionName) {
    const db = this.get();
    return db[collectionName] || [];
  }

  static updateCollection(collectionName, newArray) {
    const db = this.get();
    db[collectionName] = newArray;
    return this.save(db);
  }
}

module.exports = Database;
