import { useState } from "react";
import { Routes, Route } from "react-router-dom";
import "./styles.css";
import Home from "./pages/Home";
import Settings from "./pages/Settings";
import ViewExpenses from "./pages/ViewExpenses";
import DefineFood from "./pages/DefineFood";
import AddExpense from "./pages/AddExpense";

function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/settings" element={<Settings />} />
        <Route path="/view-expenses" element={<ViewExpenses />} />
        <Route path="/define-food" element={<DefineFood />} />
        <Route path="/add/:timeslot" element={<AddExpense />} />
      </Routes>
    </>
  );
}

export default App;
