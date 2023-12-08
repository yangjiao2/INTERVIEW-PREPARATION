// src/components/JobBoard.js
import React, { useState, useEffect } from 'react';

const JobBoard = () => {
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    const fetchJobs = async () => {
      try {
        const response = await fetch('https://hacker-news.firebaseio.com/v0/jobstories.json');
        const jobIds = await response.json();
        const latestJobIds = jobIds.slice(0, 10); // Get the latest 10 job IDs

        const jobRequests = latestJobIds.map(async (id) => {
          const jobResponse = await fetch(`https://hacker-news.firebaseio.com/v0/item/${id}.json`);
          return jobResponse.json();
        });

        const jobDetails = await Promise.all(jobRequests);
        setJobs(jobDetails);
      } catch (error) {
        console.error('Error fetching job data:', error);
      }
    };

    fetchJobs();
  }, []);

  return (
    <div>
      <h1>Latest Job Postings</h1>
      <ul>
        {jobs.map((job) => (
          <li key={job.id}>
            <strong>{job.title}</strong> - {job.url}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default JobBoard;
