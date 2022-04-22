<template>
	<nav class="main_nav">
		<h1>Rick and Morty Compare Tool</h1>
		<h3>By Tomy Poliakov</h3>
		<hr>
		<router-link to="/">Home</router-link>
		<router-link to="/about">About</router-link>
	</nav>
	<router-view />
</template>

<style>
	@import "./assets/styles.css";
</style>
