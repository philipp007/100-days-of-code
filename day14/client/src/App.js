import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import { createFetch, base, accept, parse } from 'http-client'

class App extends Component {
  constructor() {
    super();
    this.httpClient = createFetch(
      base('http://localhost:5000'),
      accept('application/json'),
      parse('json')
    );

    this.state = { todoList: [] }
  }

  componentDidMount() {
    const self = this;

    this.httpClient('/todos/').then(response => {
      const result = response.jsonData
    });

  }

  render() {
    const fetch = this.httpClient('/todos/');

    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
      </div>
    );
  }
}

export default App;
