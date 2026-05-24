function SeatGrid({
  seats,
  selectedSeats,
  handleSeatClick
}) {

  const rowLabels = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G"
  ]

  return (

    <div className="cinema-wrapper">

      <div className="screen">
        SCREEN
      </div>

      <div className="grid">

        {seats.map((row, rowIndex) => (

          <div
            className="seat-row-container"
            key={rowIndex}
          >

            <div className="row-label">
              {rowLabels[rowIndex]}
            </div>

            <div className="row">

              {row.map((seat, colIndex) => {

                const seatId =
                  `${rowIndex}-${colIndex}`

                const isSelected =
                  selectedSeats.includes(seatId)

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
                    className={`
                      seat
                      ${seat}
                      ${
                        isSelected
                          ? 'selected'
                          : ''
                      }
                    `}
                    onClick={() =>
                      handleSeatClick(
                        rowIndex,
                        colIndex,
                        seat
                      )
                    }
                  >

                    {rowLabels[rowIndex]}
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

    </div>

  )
}

export default SeatGrid