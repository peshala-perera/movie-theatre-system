function BookingInfo({
  currentUser
}) {

  return (

    <div className="booking-info">

      {
        currentUser?.type === 'vip' && (
          <p>
            VIP users get premium center seats.
          </p>
        )
      }

      {
        currentUser?.type === 'disabled' && (
          <p>
            Accessible seating prioritized.
          </p>
        )
      }

      {
        currentUser?.type === 'admin' && (
          <p>
            Admin override enabled.
          </p>
        )
      }

      {
        currentUser?.type === 'regular' && (
          <p>
            Best available regular seats.
          </p>
        )
      }

    </div>

  )

}

export default BookingInfo