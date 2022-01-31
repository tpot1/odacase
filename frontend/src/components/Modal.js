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
      activeItem: this.props.activeItem,
    };
  }

  handleChange = (e) => {
    let { name, value } = e.target;

    if (e.target.type === "checkbox") {
      value = e.target.checked;
    }

    const activeItem = { ...this.state.activeItem, [name]: value };

    this.setState({ activeItem });
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
                value={this.state.activeItem.base_url}
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
                value={this.state.activeItem.whitelist}
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
                    value={this.state.activeItem.product_xpath}
                    onChange={this.handleChange}
                    placeholder="Enter xpath to product"
                />
            </FormGroup>
          </Form>
        </ModalBody>
        <ModalFooter>
          <Button
            color="success"
            onClick={() => onSave(this.state.activeItem)}
          >
            Save
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}