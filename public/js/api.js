/**
 * RentWala - Sharma Rentals
 * Centralized API Client (REST API + LocalStorage Fallback)
 */

const API = {
  isLive: false,

  async checkHealth() {
    try {
      const res = await fetch('/api/health');
      if (res.ok) {
        this.isLive = true;
        return true;
      }
    } catch (e) {
      this.isLive = false;
    }
    return false;
  },

  async getProperties() {
    if (this.isLive) {
      try {
        const res = await fetch('/api/properties');
        if (res.ok) return await res.json();
      } catch (e) { console.warn('Fetch fallback to LocalStorage'); }
    }
    return JSON.parse(localStorage.getItem('rentwala_properties')) || DEFAULT_PROPERTIES;
  },

  async addProperty(propertyData) {
    if (this.isLive) {
      try {
        const res = await fetch('/api/properties', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(propertyData)
        });
        if (res.ok) return await res.json();
      } catch (e) { console.warn('Fallback add property'); }
    }
    return { success: true };
  },

  async updatePropertyStatus(id, status, vacantDays = 0) {
    if (this.isLive) {
      try {
        await fetch(`/api/properties/${id}`, {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ status, vacantDays })
        });
      } catch (e) { console.warn('Fallback status update'); }
    }
  },

  async deleteProperty(id) {
    if (this.isLive) {
      try {
        await fetch(`/api/properties/${id}`, { method: 'DELETE' });
      } catch (e) { console.warn('Fallback delete'); }
    }
  },

  async getTenants() {
    if (this.isLive) {
      try {
        const res = await fetch('/api/tenants');
        if (res.ok) return await res.json();
      } catch (e) { console.warn('Fallback tenants'); }
    }
    return JSON.parse(localStorage.getItem('rentwala_tenants')) || DEFAULT_TENANTS;
  },

  async bookVisit(visitData) {
    if (this.isLive) {
      try {
        const res = await fetch('/api/visits', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(visitData)
        });
        if (res.ok) return await res.json();
      } catch (e) { console.warn('Fallback book visit'); }
    }
    return { success: true, bookingId: 'VISIT-' + Math.floor(1000 + Math.random() * 9000) };
  },

  async payToken(tokenData) {
    if (this.isLive) {
      try {
        const res = await fetch('/api/token', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(tokenData)
        });
        if (res.ok) return await res.json();
      } catch (e) { console.warn('Fallback pay token'); }
    }
    return { success: true };
  },

  async getMaintenance() {
    if (this.isLive) {
      try {
        const res = await fetch('/api/maintenance');
        if (res.ok) return await res.json();
      } catch (e) { console.warn('Fallback maintenance'); }
    }
    return JSON.parse(localStorage.getItem('rentwala_complaints')) || DEFAULT_COMPLAINTS;
  },

  async addComplaint(complaintData) {
    if (this.isLive) {
      try {
        const res = await fetch('/api/maintenance', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(complaintData)
        });
        if (res.ok) return await res.json();
      } catch (e) { console.warn('Fallback add complaint'); }
    }
    return { success: true };
  }
};
