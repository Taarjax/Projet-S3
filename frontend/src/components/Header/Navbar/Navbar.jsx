import React, { useState, useEffect } from "react";
import "./Navbar.css";

import "../../variables.css";
import Button from "../../Button";
import NavBarMobile from "./NavbarMobile";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBars } from "@fortawesome/free-solid-svg-icons";

import { NavLink } from "react-router-dom";
import { getUser } from "../../Axios/Axios";

function Navbar() {
  const [classNav, setStateClassNav] = useState("navbar-mobile none");
  const [user, setUser] = useState(undefined);

  const action_bars = (e) => {
    e.preventDefault();
    setStateClassNav("navbar-mobile slide_to_left");
  };

  const action_cross = (e) => {
    e.preventDefault();
    setStateClassNav("navbar-mobile slide_to_right");
  };

  const get_user = async function () {
    let u = await getUser();

    if (JSON.stringify(u) !== JSON.stringify(user)) {
      setUser(u);
    }
  };

  const log_buttons = function () {
    if (user) {
      return (
        <NavLink to="/deconnexion">
          <li>
            <i className="fas fa-user"></i>
            <a href="#/">Déconnexion</a>
          </li>
        </NavLink>
      );
    } else {
      return (
        <NavLink to="/connexion">
          <li>
            <i className="fas fa-user"></i>
            <a href="#/">connexion</a>
          </li>
        </NavLink>
      );
    }
  };

  useEffect(() => {
    get_user();
  });

  return (
    <div className="navbar">
      <nav>
        <div className="navbar-container">
          <NavLink to="/">
            <div className="navbar-logo">
              <i className="fas fa-glass-martini-alt"></i>
              <span className="navbar-logo-title">Shaker Magique</span>
            </div>
          </NavLink>
          <div className="navbar-navlinks">
            <NavLink to="/rejoindre-hote">
              <li>
                <i className="fas fa-user-friends"></i>
                <a href="#/">rejoindre un hôte</a>
              </li>
            </NavLink>
            {log_buttons()}
          </div>
          <Button
            content={<FontAwesomeIcon icon={faBars} />}
            class_name="btn-bars"
            action={action_bars}
          ></Button>
        </div>
        <NavBarMobile class_name={classNav} action_cross={action_cross} />
      </nav>
    </div>
  );
}

export default Navbar;
