import { useParams } from "react-router-dom";

function AddExpense() {
  const { timeslot } = useParams(); // Get "morning", "afternoon", etc.

  return (
    <div>
      <h2>Add Expense for: {timeslot.toUpperCase()}</h2>

      {/* Load available foods */}
      {/* Allow selecting food items */}
      {/* Submit selected foods to backend with the timeslot info */}
    </div>
  );
}

export default AddExpense;
