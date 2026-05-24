function Counter({
  groupSize,
  setGroupSize,
  currentUser
}) {

  return (
    <div className="group-size-box">

      <label>
        Group Size
      </label>

      <div className="group-controls">

        <button onClick={() => setGroupSize(Math.max(1, groupSize - 1)) }> - </button>

        <span>{groupSize}</span>

        <button onClick={() => setGroupSize(groupSize + 1) } > + </button>

      </div>

    </div>
  )

}

export default Counter