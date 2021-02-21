import logo from './logo.svg';
import './App.css';
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css'
import {Container, Row, Col, Button, Alert, Breadcrumb, Card, Form} from 'react-bootstrap'
//import { PieChart } from 'react-minimal-pie-chart';





function App() {
  return (
    <div className="App">
      <h1 margin-bottom="10px"> UnivestIQ Demo</h1>
      <header className="App-header">
        {/* <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p> */}
        
          <Form>
            <Form.Group>
              <Form.Label>Email Address</Form.Label>
              <Form.Control type="email" placeholder="Example@email.com"></Form.Control>
              <Form.Text className="text-muted"> Don't worry, we'll never share your email</Form.Text>
            </Form.Group>
          </Form>
        
        <Card className= "mb-3" style = {{ color: "#000"}}>
          <Card.Img src="./Pie-Chart.jpg"/>
          <Card.Body>
            <Card.Title>
              Card Example
            </Card.Title>
            <Card.Text>
              This is an example of react bootstrap cards.
            </Card.Text>
          </Card.Body>
        </Card>
        <Button> Test Button </Button>
     
        
        
        {/* <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a> */}
      </header>
    </div>
  );
}

export default App;
