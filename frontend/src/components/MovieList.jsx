function MovieList({
  movies,
  selectedMovie,
  setSelectedMovie
}) {

  return (

    <div className="movies">

      {
        movies.map((movie, index) => (

          <div
            key={index}
            className={`
              movie-card
              ${
                selectedMovie === movie.title
                  ? 'selected-movie'
                  : ''
              }
            `}
            onClick={() =>
              setSelectedMovie(movie.title)
            }
          >

            <img
              src={movie.poster}
              alt={movie.title}
            />

            <p>
              {movie.title}
            </p>

          </div>

        ))
      }

    </div>

  )

}

export default MovieList