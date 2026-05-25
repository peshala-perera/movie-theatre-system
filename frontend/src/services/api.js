import axios from 'axios'

const API =
  'http://127.0.0.1:5000'

export const fetchSeatsApi =
  async (movie) => {

    const response =
      await axios.get(
        `${API}/seats`,
        {
          params: { movie }
        }
      )

    return response.data

  }

export const allocateSeatsApi =
  async (data) => {

    const response =
      await axios.post(
        `${API}/allocate`,
        data
      )

    return response.data

  }