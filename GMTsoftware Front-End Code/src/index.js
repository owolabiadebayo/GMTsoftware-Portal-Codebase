import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import { initialState } from "./reducer/reducer";
import { StateProvider } from "./stateProvider/stateProvider";
import reducer from "./reducer/reducer";

ReactDOM.render(
  <React.StrictMode>
    <StateProvider initialState={initialState} reducer={reducer}>
      <App />
    </StateProvider>
  </React.StrictMode>,
  document.getElementById("root")
);