import React, { Component } from "react";
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Input,
  Label,
} from "reactstrap";

export default class CustomModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
        configItem: this.props.configItem,
        configAttributes: this.props.configAttributes,
    };
  }

  handleChange = (e, attributeId=null) => {
    let { name, value } = e.target;

    if (e.target.type === "checkbox") {
      value = e.target.checked;
    }

    if (attributeId) {
        const configAttributes = this.state.configAttributes.map(a => a.id === attributeId ? { ...a, [name]: value } : a);

        this.setState({ configAttributes });
    }
    else {
        const configItem = { ...this.state.configItem, [name]: value };

        this.setState({ configItem });
    }

  };

  render() {
    const { toggle, onSave } = this.props;

    return (
      <Modal isOpen={true} toggle={toggle}>
        <ModalHeader toggle={toggle}>Config Item</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="config-base-url">Base URL</Label>
              <Input
                type="text"
                id="config-base-url"
                name="base_url"
                value={this.state.configItem.base_url}
                onChange={this.handleChange}
                placeholder="Enter config base URL"
              />
            </FormGroup>
            <FormGroup>
              <Label for="config-whitelist">Whitelist</Label>
              <Input
                type="text"
                id="config-whitelist"
                name="whitelist"
                value={this.state.configItem.whitelist}
                onChange={this.handleChange}
                placeholder="Enter config whitelist"
              />
            </FormGroup>
            <FormGroup>
              <Label for="config-xpath">Product x-path</Label>
                <Input
                    type="text"
                    id="config-xpath"
                    name="product_xpath"
                    value={this.state.configItem.product_xpath}
                    onChange={this.handleChange}
                    placeholder="Enter xpath to product"
                />
            </FormGroup>
            {this.state.configAttributes.map(attribute => {
                return (
                  <div key={attribute.attribute_name}>
                  <FormGroup>
                    <Label for="attribute_name">Attribute Name</Label>
                      <Input
                          type="text"
                          id="attribute_name"
                          name="attribute_name"
                          value={attribute.attribute_name}
                          onChange={(e) => this.handleChange(e, attribute.id)}
                          placeholder="Enter attribute name"
                      />
                  </FormGroup>
                  <FormGroup>
                    <Label for="attribute_xpath">Attribute x-path</Label>
                      <Input
                          type="text"
                          id="attribute_xpath"
                          name="attribute_xpath"
                          value={attribute.attribute_xpath}
                          onChange={(e) => this.handleChange(e, attribute.id)}
                          placeholder="Enter attribute x-path"
                      />
                  </FormGroup>
                  </div>);
            })}
          </Form>
        </ModalBody>
        <ModalFooter>
          <Button
            color="success"
            onClick={() => onSave(this.state.configItem, this.state.configAttributes)}
          >
            Save
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}