<template>
	<div id="contents">
		<h1 v-if="selected === 'home'"> <Home/> </h1>
		<h1 v-else-if="selected === 'negative'"> <Negative/> </h1>
		<h1 v-else-if="selected === 'exposure'"> <Exposure/> </h1>
		<h1 v-else-if="selected === 'about'"> <About/> </h1>
	</div>
</template>

<script>
import Home from './Home.vue'
import Negative from './Negative.vue'
import Exposure from './Exposure.vue'
import About from './About.vue'

export default {
  name: 'Contents',
  props: [ 'selected' ],
  components: { Home, Negative, Exposure, About }
}
</script>

<style scoped>
	#contents {
		flex-grow: 4;
        color: #eeeeee;
        display: inline-block;
        background-color: #534c00;
	}
</style>

