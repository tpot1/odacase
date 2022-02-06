import React, { Component } from "react";
import Modal from "./components/Modal";
import axios from "axios";

class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      configItems: [],
      configAttributes: [],
      modal: false,
      activeItemId: null,
    };
  }

  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios
      .get("/api/config/")
      .then((res) => {
        this.setState({ configItems: res.data })
      })
      .catch((err) => console.log(err));
    axios
      .get("/api/attribute/")
      .then((res) => {
        this.setState({ configAttributes: res.data })
      })
      .catch((err) => console.log(err));
  };

  toggle = () => {
    this.setState({ modal: !this.state.modal });
  };

  handleSubmit = (item, attributes) => {
    this.toggle();

    let promises = [];

    attributes.forEach(a => {
      if (a.id) {
        promises.push(axios.put(`/api/attribute/${a.id}/`, a));
      }
      else {
        promises.push(axios.post("/api/attribute/", a));
      }
    })

    if (item.id) {
      promises.push(axios.put(`/api/config/${item.id}/`, item));
    }
    else {
      promises.push(axios.post("/api/config/", item));
    }

    Promise.all(promises).then((res) => this.refreshList());
    
  };

  handleDelete = (item) => {
    axios
      .delete(`/api/config/${item.id}/`)
      .then((res) => this.refreshList());
  };

  createItem = () => {
    const item = { base_url: "", whitelist: "", product_xpath: "" };

    this.setState({ activeItemId: item.id, modal: !this.state.modal });
  };

  editItem = (item) => {
    this.setState({ activeItemId: item.id, modal: !this.state.modal });
  };


  renderItems = () => {

    return this.state.configItems.map((item) => (
      <li
        key={item.base_url}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className={`config-title mr-2`}
        >
          {item.base_url}
        </span>
        <span>
          <button
            className="btn btn-secondary mr-2"
            onClick={() => this.editItem(item)}
          >
            Edit
          </button>
          <button
            className="btn btn-danger"
            onClick={() => this.handleDelete(item)}
          >
            Delete
          </button>
        </span>
      </li>
    ));
  };

  render() {
    return (
      <main className="container">
        <h1 className="text-white text-uppercase text-center my-4">Product scraper configurations</h1>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="mb-4">
                <button
                  className="btn btn-primary"
                  onClick={this.createItem}
                >
                  Add configuration
                </button>
              </div>
              <ul className="list-group list-group-flush border-top-0">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
        {this.state.modal ? (
          <Modal
            configItem={this.state.configItems.find(a => a.id === this.state.activeItemId)}
            configAttributes={this.state.configAttributes.filter(a => a.ps_config === this.state.activeItemId)}
            toggle={this.toggle}
            onSave={this.handleSubmit}
          />
        ) : null}
      </main>
    );
  }
}

export default App;