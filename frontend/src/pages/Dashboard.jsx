import React, { useEffect, useState } from 'react';
import FleetMap from '../components/FleetMap';
import DeliveryStats from '../components/DeliveryStats';

const Dashboard = () => {
  const [fleetData, setFleetData] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/fleet/status')
      .then((res) => res.json())
      .then((data) => setFleetData(data))
      .catch((err) => console.error('Error fetching fleet data:', err));
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Fleet Dashboard</h1>
      <DeliveryStats data={fleetData} />
      <FleetMap data={fleetData} />
    </div>
  );
};

export default Dashboard;
