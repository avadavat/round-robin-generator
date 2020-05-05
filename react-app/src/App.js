import React, { Component } from "react";
import "./App.css";
import NavBar from "./components/navbar";
import Teams from "./components/teamTextbox";
// import * as ReactBootStrap from "react-bootstrap";
class App extends Component {
  state = {
    teams: [],
    text_value: "",
    is_loading: false,
    result: "empty",
  };

  handleSubmit = (event) => {
    // this.setState({ teams: ["team3", "team4"] });
    event.preventDefault();
    const data = this.state.text_value;
    console.log(this.state.result);
    this.setState({ teams: data.split(",") });
    this.setState({ isLoading: true });
    fetch("http://127.0.0.1:5000/datapage/", {
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      method: "POST",
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((response) => {
        this.setState({
          result: response.result,
          isLoading: false,
        });
      });
  };

  handleInputChange = (event) => {
    event.preventDefault();
    this.setState({
      [event.target.name]: event.target.value,
    });
  };

  fillCols = () => {
    this.result["columns"].map();
  };

  render() {
    return (
      <React.Fragment>
        <NavBar />
        <main className="container">
          <Teams
            onSubmit={this.handleSubmit}
            onChange={this.handleInputChange}
            name="text_value"
          ></Teams>
        </main>
        <p> Entry: {this.state.teams}</p>
        <br></br>
        <h6> Result: {this.state.result}</h6>
        {/* <table class="table">
          <thead>
            <tr>
              <th scope="col">Col1</th>
              <th scope="col">Col2</th>
            </tr>
          </thead>
          <tbody></tbody>
        </table> */}
      </React.Fragment>
    );
  }
}

export default App;
