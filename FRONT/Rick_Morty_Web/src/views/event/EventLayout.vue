<template>
	<div class="container">
		<div class="card_single">
			<img :src="event ? event.image : ''" class="char-image"/>
			<img :src="event ? event.image : ''" class="image-bg"/>
			<div class="information">
				<h4>{{ event ? event.name : "" }}</h4>
				<div class="status">
					<span
						:class="
							statusColor == 'Unknown'
								? ''
								: statusColor == 'Alive'
								? 'statusGreen'
								: 'statusRed'
						"
					></span>
					<span>Status: {{ event ? event.status : "" }}</span>
				</div>
			</div>
			<nav class="nav-details">
				<router-link :to="{ name: 'EventDetails' }"
					>Details</router-link
				>
				|
				<router-link :to="{ name: 'EventLocation' }"
					>Location</router-link
				>
			</nav>
			<router-view :event="event" />
		</div>
	</div>
</template>
<script>
import EventService from "@/services/EventService.js";
export default {
	props: ["id"],
	data() {
		return {
			event: null,
			statusColor: null
		};
	},
	created() {
		EventService.getEvent(this.id)
			.then((response) => {
				this.event = response.data;
				this.statusColor = this.event.status;
				//console.log(this.event.status);
			})
			.catch((error) => {
				console.log(error);

				this.$router.push({
					name: "404Resource",
					params: { resource: "event" }
				});
			});
	}
};
</script>

<style>
	@import "../../assets/styles.css";
</style>
