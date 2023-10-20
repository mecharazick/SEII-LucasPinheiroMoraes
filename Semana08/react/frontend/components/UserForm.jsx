import React from "react";
import axios from "axios";

export default class UserForm extends React.Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
    this.store = this.store.bind(this);
    this.formRef = null;
  }

  state = {
    name: "",
  };
  handleChange(e) {
    this.setState({ name: e.target.value });
  }

  store(e) {
    e.preventDefault();

    const user = axios.post("http://localhost:5000/user/add", {
      name: this.state.name,
    });
    this.formRef.reset();
  }

  render() {
    return (
      <div className="card">
        <div className="card-body shadow">
          <form onSubmit={this.store} ref={(ref) => (this.formRef = ref)}>
            <div className="form-group row">
              <label htmlFor="inputEmail3" className="col-sm-2 col-form-label">
                Name
              </label>
              <div className="col-sm-10">
                <input
                  type="text"
                  className="form-control"
                  placeholder="Name"
                  value={this.state.name}
                  onChange={this.handleChange}
                />
              </div>
            </div>
            <div className="form-group row">
              <div className="col-sm-10 offset-sm-2">
                <button type="submit" className="btn btn-primary">
                  ADD
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    );
  }
}
