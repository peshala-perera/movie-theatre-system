function Legend() {
  return (
    <div className="legend">
      <div><span className="seat O">O</span> Available</div>
      <div><span className="seat X">X</span> Booked</div>
      <div><span className="seat V">V</span> VIP</div>
      <div><span className="seat B">B</span> Broken</div>
      <div><span className="seat D">D</span> Disability</div>
      <div><span className="seat N">N</span> No-children area</div>
    </div>
  )
}

export default Legend