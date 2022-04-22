<template>
	<router-link
		class="event-link"
		:to="{
			name: 'EventDetails',
			params: { id: event.id }
		}"
	>
		<div class="event-card">
			<img :src="event.image" class="char-image"/>
			<img :src="event.image" class="image-bg"/>
			<div class="information">
				<h4 class="char_name">{{ event.name }}</h4>
				<h4 class="char_id">Character ID: {{ event.id }}</h4>
				<div class="status">
					<!-- <span v-if="statusColorR" class="status-icon-r"></span>
					<span v-else-if="statusColorG" class="status-icon-g"></span> -->
					<span><b>Status: </b> 
						<span v-if="statusColorR" class="status-text-r">{{ event.status }} <i class="fa-solid fa-face-dizzy"></i></span>
						<span v-else-if="statusColorG" class="status-text-g">{{ event.status }} <i class="fa-solid fa-face-smile"></i></span>
						<span v-else class="status-text-u">{{ event.status }} <i class="fa-solid fa-face-meh"></i></span>
					</span>
				</div>
				<span class="char_btn">Read More...</span>
			</div>
		</div>
	</router-link>
</template>

<script>
export default {
	props: {
		event: {
			type: Object,
			required: true
		}
	},
	data() {
		return {
			status: this.event.status
		};
	},
	computed: {
		statusColorR() {
			if (this.status === "Dead") {
				return 1;
			} else return 0;
		},
		statusColorG() {
			if (this.status === "Alive") {
				return 1;
			} else return 0;
		}
	}
};
</script>

<style>
	@import "../assets/styles.css";
</style>
