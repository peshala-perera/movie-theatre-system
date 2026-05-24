function Controls({
  groupSize,
  setGroupSize,
  allocateSeats,
  bookSelectedSeats
}) {

  return (

    <div className="controls">

      <input
        type="number"
        min="1"
        max="7"
        value={groupSize}
        onChange={(e) =>
          setGroupSize(e.target.value)
        }
        placeholder="Group Size"
      />

      <button 
        className="auto-book-btn"
        onClick={allocateSeats}>
        Auto Allocate Seats
      </button>

      <button
        className="manual-book-btn"
        onClick={bookSelectedSeats}
      >
        Manual Allocate Seats
      </button>

    </div>

  )
}

export default Controls