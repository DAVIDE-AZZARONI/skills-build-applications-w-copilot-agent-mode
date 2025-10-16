import React, { useEffect, useState } from 'react';

const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    console.log('Fetching from:', API_URL);
    fetch(API_URL)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        console.log('Fetched activities:', results);
        setActivities(results);
      });
  }, []);

  return (
    <div className="container mt-4">
      <h2 className="mb-4 display-6">Activities</h2>
      <div className="card">
        <div className="card-body">
          <table className="table table-striped table-hover">
            <thead className="table-dark">
              <tr>
                <th>Type</th>
                <th>Duration (min)</th>
                <th>Calories</th>
              </tr>
            </thead>
            <tbody>
              {activities.map(a => (
                <tr key={a.id}>
                  <td>{a.type}</td>
                  <td>{a.duration}</td>
                  <td>{a.calories}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Activities;
