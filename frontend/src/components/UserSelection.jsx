function UserSelection({
  users,
  selectedUser,
  setSelectedUser
}) {

  return (

    <div className="user-selection">

      {
        users.map((user) => (

          <div
            key={user.name}
            className={`
              user-card
              ${
                selectedUser === user.name
                  ? 'active-user'
                  : ''
              }
            `}
            onClick={() =>
              setSelectedUser(user.name)
            }
          >

            <strong>
              {user.name}
            </strong>

            <span>
              {user.type}
            </span>

          </div>

        ))
      }

    </div>

  )

}

export default UserSelection