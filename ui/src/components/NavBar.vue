<template>
	<div id="navbar">
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
	#navbar {
        flex-basis: 100%;
        background-color: #003153;
        /* border-bottom: 10px solid #333333; */
	}

	#navbar ul {
		display: flex;
        flex-flow: row wrap;
        justify-content: flex-start;
        list-style: none;
        margin: 0px;
        color: white;
		font-weight: bold;
	}

	#navbar li {
		color: white;
		background-color: inherit;
		display: inline-block;
		cursor: pointer;
        padding: 1rem;
        display: block;
	}
	#navbar li:hover{
		color: #003153;
		background-color: white;
	}
	
	#navbar li.selected{
		background-color: #530008;
		color: white;
	}
</style>

