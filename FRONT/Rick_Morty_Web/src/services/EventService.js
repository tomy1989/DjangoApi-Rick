import axios from "axios";
//Doing some axios req
const RickapiClient = axios.create({
	baseURL: "https://rickandmortyapi.com/api/character",
	withCredentials: false,
	headers: {
		Accept: "application/json",
		"Content-Type": "application/json"
	}
});
const MyapiClientCompare = axios.create({
	baseURL: "http://localhost:8000/api/charachters/compare",
	withCredentials: false,
	headers: {
		Accept: "application/json",
		"Content-Type": "application/json"
	}
});

const MyapiClientCompareCsv = axios.create({
	baseURL: "http://127.0.0.1:8000/api/charachters/compare_to_csv",
	withCredentials: false,
	headers: {
		Accept: "application/json",
		"Content-Type": "application/json"
	}
});
export default {
	getEvents() {
		return RickapiClient.get("/");
	},
	getEventsPage(page) {
		return RickapiClient.get("?page=" + page);
	},
	getEvent(id) {
		return RickapiClient.get("/" + id);
	},

	//Getting our compare data
	getCompare(data) {
		return MyapiClientCompare.get("/" + data);
	},
	getCompareCsv(data) {
		return MyapiClientCompareCsv.get("/" + data);
	}
};
