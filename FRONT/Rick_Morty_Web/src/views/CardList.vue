<template>
	<div class="search_box">
		<div class="btn-container">
			<div class="search_bar">
				<input v-model="message" @keypress="isNumber($event)" placeholder="Enter ID Number...">
				<button v-on:click="doCompare" class="search_btn"><i class="fa-solid fa-magnifying-glass"></i></button>
			</div>
			<h3 class="search_hint"><i class="fa-solid fa-circle-exclamation"></i> Enter character ID split with ,</h3>
			<div class="search_selections">
				<input type="radio" id="one" value='1' v-model="picked" />
				<label for="one">Csv</label>
				<input type="radio" id="two" value='0' v-model="picked" />
				<label for="two">Regular</label>
			</div>
		</div>
	</div>
	<!-- btns -->
	<div class="navigation-container">
		<button v-on:click="prevPage"><i class="fa-solid fa-angle-left"></i> Prev</button>
		<button v-on:click="nextPage">Next <i class="fa-solid fa-angle-right"></i></button>
		<button v-if="Backbtntrigger" v-on:click="getPage">Back</button>
	</div>
	<!-- POPUP -->
	<popup v-if="poptrigger" :TogglePopup="() => TogglePopup()">
		<h1>{{popupMsg}}</h1>
		<hr style="margin:1rem; border:none;">
		<a class="button download_btn" v-if="Csvtrigger" :href="filePath" download>Download your CSV</a>
	</popup>
	<div class="container">
		<EventCard v-for="event in events" :key="event.id" :event="event" />
	</div>
</template>

<script>
// @ is an alias to /src
import EventCard from "@/components/EventCard.vue";
import EventService from "@/services/EventService.js";
import popup from "@/components/EventPopup.vue"
//import {ref} from 'vue';

//import axios from 'axios'
export default {

	setup(){
		
		/*const PopupTrigger = ref({
			btnTrigger: false
		})*/
	},
	//props: ["page"],
	name: "CardList",
	components: {
		EventCard,
		popup,

	},
	data() {
		return {
			events: null,
			popupMsg: '',
			page: 1,
			picked: '0',
			message: '',
			poptrigger: false,
			Backbtntrigger: false,
			filePath: '',
			Csvtrigger: false
		};
	},
	created() {
		
		EventService.getEvents()
			.then((response) => {
				console.log("events:", response.data.results);
				this.events = response.data.results;
			})
			.catch((error) => {
				console.log(error);
			});
	},
	methods: {
		TogglePopup: function(){
			this.poptrigger = !this.poptrigger
		},
		ToggleCsv: function(){
			this.Csvtrigger = !this.Csvtrigger
		},
		//Go next page function
		nextPage: function () {
			this.page++;
			this.getPage();
		},
		//Go prev page function
		prevPage: function () {
			this.page < 2 ? this.page : this.page--;
			this.getPage();
		},
		//Get compare information
		doCompare: function(){
			console.log(this.picked)
			//make sure user input at least 2 characters
			if(this.message.length >= 3)
			{
				//check user want csv or regular output
				this.picked === '0' ?  this.getCompare() : this.getCsv()
			}
			else{
				this.popupMsg = 'Please Enter minimum 2 characters';
				this.TogglePopup();
			}
		},
		//Function to ensure user input only alowed chachters
		isNumber: function(evt) {
			evt = (evt) ? evt : window.event;
			var charCode = (evt.which) ? evt.which : evt.keyCode;
			/*Allow to user insert only digit and , */
			if ((charCode > 31 && (charCode < 48 || charCode > 57)) && charCode !== 44) {
				evt.preventDefault();
			} else {
				return true;
			}
		},
		//Getting page with characters from rick api
		getPage: function () {
			this.Backbtntrigger = false
			this.Csvtrigger = false
			EventService.getEventsPage(this.page)
				.then((response) => {
					//console.log("events:", response.data.results);
					this.events = response.data.results;
				})
				.catch((error) => {
					console.log(error);
				});
		},
		//start getting compare information
		getCompare: function () {
			console.log("doing compare")
			this.Csvtrigger = false
			EventService.getCompare(this.message)
				.then((response) => {
					console.log("events:", response.data);
					console.log(response.data['characters']);
					this.events = response.data['characters'];
					console.log('dsfd')
					console.log(response.data['result']['result'])
					response.data['result']['result'] === true
						? this.popupMsg = 'Great! Characters are identical' 
						: this.popupMsg = 'unfortunately! Characters are not similar';
					this.TogglePopup()
					this.Backbtntrigger = true
				})
				.catch((error) => {
					this.errorHandle(error)
				});
		},
		//getting csv file compare
		getCsv: function () {
			console.log("doing csv compare")
			EventService.getCompareCsv(this.message)
				.then((response) => {
					console.log("events:", response.data);
					console.log(response.data['file']);

					this.popupMsg = 'Great! Your csv here: ' + response.data['file']
					this.filePath = response.data['file']
					this.TogglePopup()
					this.Backbtntrigger = true
					this.Csvtrigger = true
				})
				.catch((error) => {
					this.errorHandle(error)
				});
		},
		//handle some errors
		errorHandle: function(error)
		{
			console.log(error);
					if (error.response) {
						console.log(error.response);
						console.log(error.message);
						console.log(error.response.statusText);
						console.log(error.response.data)
						if(error.response.data['Error msg'])
						{
							error.response.data['Error msg'] === "invalid literal for int() with base 10: ''" 
							? this.popupMsg = 'Please make sure you have entered right format search' 
							: this.popupMsg = error.response.data['Error msg'];
						}
						else if(error.response.data['Something went wrong more information'])
						{
							this.popupMsg = error.response.data['Something went wrong more information']
						}
						else
						{
							error.response.statusText === 'Bad Request' 
							? this.popupMsg = 'Please make sure you have entered right format search' 
							: this.popupMsg = 'We got error try again later';
						}
						
						this.TogglePopup();
					}
					else{
						console.log('Error', error.message);
					}
		}
		
	}
};
</script>

<style>
	@import "../assets/styles.css";
</style>
