function SeatGrid({
  seats
}) {

  const rowLabels = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O"
  ]

  return (

    <div className="cinema-wrapper">

      <div className="grid">

        {seats?.map((row, rowIndex) => (

          <div
            className="seat-row-container"
            key={rowIndex}
          >

            <div className="row-label">
              {rowLabels[rowIndex]}
            </div>

            <div className="row">

              {row.map((seat, colIndex) => {

                if (seat === " ") {

                  return (
                    <div
                      key={colIndex}
                      className="aisle"
                    />
                  )

                }

                return (

                  <div
                    key={colIndex}
                    className={`seat ${seat}`}
                  >

                    {colIndex + 1}

                  </div>

                )

              })}

            </div>

            <div className="row-label">
              {rowLabels[rowIndex]}
            </div>

          </div>

        ))}

      </div>

      <div className="screen">
        SCREEN
      </div>

    </div>

  )

}

export default SeatGrid