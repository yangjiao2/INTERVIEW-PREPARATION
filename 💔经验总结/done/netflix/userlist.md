import React, { useState } from 'react'
import ReactDOM from 'react-dom'
import './App.css'
import { userList } from './userList';

function App() {

  const [userlist, setUserlist] = useState(userList);
  const  [reverse, setReverse] = useState({
    id: 0,
    firstName: 0,
    lastName: 0,
    age: 0
  })

  const onSort = (field) => {

    setReverse({
      ...reverse,
      [field]: reverse[field] != 0 ? reverse[field] * -1: 1
    })
  
    setUserlist([...userList].sort((a,b) => 
    {
      if (field == 'firstName' || field == 'lastName'){
        return reverse[field] != 0 ? reverse[field] * a[field].localeCompare(b[field]) : a[field].localeCompare(b[field]);
      } else {
        return  reverse[field] != 0 ? reverse[field] * (a[field] > b[field] ? 1: -1) : a[field] > b[field] ? 1: -1;
      }
      
    }));
  }


  return (
    <div className="app">
      <table>
        <thead>
          <tr>
            <th onClick={() => onSort('id')}>ID</th>
            <th onClick={() => onSort('firstName')}>First Name</th>
            <th onClick={() => onSort('lastName')}>Last Name</th>
            <th onClick={() => onSort('age')}>Age</th>
          </tr>
        </thead>
        
        <tbody>
          {userlist.map((r) => (
            <tr key={r.id}>
              <td>{r.id}</td>
              <td>{r.firstName}</td>
              <td>{r.lastName}</td>
              <td>{r.age}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}






ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
)



body {
    height: 100%;
    margin: 0;
    font-family: 'Roboto', Arial, sans-serif;
    font-size: 1.2rem;
  }
  
  .app {
    color: #353C4E;
    background: #F0F2F4;
    width: 100%;
  }
  
  table {
    border-collapse: collapse;
    margin: 0 auto;
  }
  
  table thead{
    position: sticky;
    top: 0;
    background-color: white;
  }
  
  table th {
      padding: 4px 10px;
  }
  
  table td {
    padding: 4px 10px;
  }
  
  table tr:nth-child(even){
    background-color: lightblue;
  }
  
  
  