<template>
	<div id="contents">
		<h1> content </h1>
		lorem ipsulum blau {{ selected }}
	</div>
</template>

<script>
export default {
  name: 'Contents',
  props: [ 'selected' ]
}
</script>

<style scoped>
	#contents {
		padding: 20px;
		width: 75%;
        color: #eeeeee;
        background-color: #534c00;
	}
</style>

