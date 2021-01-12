import React, { useEffect, useState } from "react";
import "./AdminIngredientPage.css";
import AdminIngredientFilter from "./AdminIngredientFilter";
import AdminIngredientTable from "./AdminIngredientTable";
import { apiGetIngredients, usePermission } from "../../Axios/Axios";
import { useHistory } from "react-router-dom";

export default function AdminIngredientPage() {
  const isAdmin = usePermission("admin");
  const history = useHistory();

  if (!isAdmin) history.replace("/");

  const [ingredients, setIngredients] = useState([]);
  const [search, setSearch] = useState();

  useEffect(() => {
    async function selfFunction() {
      setIngredients(await apiGetIngredients());
    }
    selfFunction();
  }, []);

  const handleSearch = (search) => {
    setSearch(search);
  };
  return (
    <div className="page admin-ingredients-page">
      {isAdmin && (
        <div className="admin-ingredients-page-container">
          <AdminIngredientFilter onSearch={handleSearch} />
          <AdminIngredientTable ingredients={ingredients} search={search} />
        </div>
      )}
    </div>
  );
}
