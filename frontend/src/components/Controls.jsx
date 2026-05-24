function Controls({
  openAutoModal
}) {

  return (

    <div className="controls">

      <button
        className="auto-book-btn"
        onClick={openAutoModal}
      >

        Auto Allocate Seats

      </button>

    </div>

  )

}

export default Controls