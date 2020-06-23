<template>
	<div id="sidebar">
		<ul>
			<li v-on:click="$emit('sel-nav', 'home')" v-bind:class="{ selected: homeSelected }"> Home </li>
			<li v-on:click="$emit('sel-nav', 'negative')"  v-bind:class="{ selected: negativeSelected }"> Negativo </li>
			<li v-on:click="$emit('sel-nav', 'exposure')" v-bind:class="{ selected: exposureSelected }"> Exposição </li>
			<li v-on:click="$emit('sel-nav', 'about')" v-bind:class="{ selected: aboutSelected }"> Sobre </li>
		</ul>
	</div>
</template>

<script>
export default {
	name: 'SideBar',
	props: [ 'selected' ],
	computed: {
		homeSelected: function(){ return this.selected === 'home'; },
		negativeSelected: function(){ return this.selected === 'negative'; },
		exposureSelected: function(){ return this.selected === 'exposure'; },
		aboutSelected: function() { return this.selected === 'about'; }
	}

}
</script>

<style scoped>
	#sidebar {
		padding: 24px;
		width: 25%;
		float: left;
		background-color: #003153;
		border-right: 10px solid #333333;
	}

	#sidebar ul {
		color: white;
		font-weight: bold;
		padding: 1rem;
	}

	#sidebar li {
		color: white;
		background-color: inherit;
		display: inline-block;
		padding: 2rem;
		width: 100%;
		cursor: pointer;

	}
	#sidebar li:hover{
		color: #003153;
		background-color: white;
	}
	
	#sidebar li.selected{
		background-color: #530008;
		color: white;
	}
</style>

