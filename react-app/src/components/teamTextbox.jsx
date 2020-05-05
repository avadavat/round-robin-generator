import React, { Component } from "react";

class Teams extends Component {
  render() {
    return (
      <div>
        <h4>Please enter a comma separated list of players or teams.</h4>
        <form onSubmit={(event) => this.props.onSubmit(event)}>
          <p>
            <input
              type="text"
              placeholder="Enter text here"
              name={this.props.name}
              onChange={(event) => this.props.onChange(event)}
            />
          </p>
          <button className="btn btn-danger btn-sm m-2">Submit teams</button>
        </form>
      </div>
    );
  }
}

export default Teams;
