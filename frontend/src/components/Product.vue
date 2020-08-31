<template>
<div class="Product">
	<div class="Product-figure">
		<img v-bind:src="'http://cdn.agbdining.com/'+product.imageUrl" class="Product-image">
		<button v-on:click="addToCart()" class="Product-button">Sepete ekle</button>
	</div>
	<div class="Product-body">
		<h3 class="Product-title">{{ product.name }}</h3>
		<p class="Product-description">{{ product.description }}</p>
		<div class="Product-Price">
			{{ product.price }}
		</div>
	</div>
</div>
</template>

<script>
export default {
	name: 'Product',
	props:  {
		product: Object
	},
	methods: {
		addToCart: function () {
			this.$emit('AddToCart', this.product)
		}
	},
}
</script>

<style>

.Product {
	background: #fff;
	border: 1px solid hsla(0, 0%, 0%, 0.1);
	border-radius: 4px;
	display: flex;
	flex-flow: row;
	min-width: 0;
	overflow: hidden;
	padding: 1em;
	position: relative;
	transition: flex-grow 0.5s;
	min-width: 0;
	flex: 5;
	border-right: 1px solid #eee;
	margin-bottom: 0;
	padding-right: 1em;
}

.Product-figure {
	width: 100%;
	min-width: 130px;
	border-right: 1px solid #eee;
	flex: 2;
	margin-right: 1em;
	margin-bottom: 0;
	padding-right: 1em;
}

.Product-body :last-child {
	margin-bottom: 0;
    min-width: 0;
	flex: 5;
}

.Product-title {
	margin-top: 0px;
	font-weight: 600;
	font-size: 1.4em;
	margin-bottom: calc(.75em / 1.4);
}

.Product-image {
	max-width: 120px;
	border: 1px solid hsl(0, 0%, 90%);
	padding: .25em;
}

.Product-button {
	margin-top:8px;
	margin-bottom : 0px;
	height: 30px;
	width :90px;
	background-color: rgb(231, 231, 231);
	border: 1px solid #777;
	border-radius: 5px;
	padding: .25em;
}

.Product-button:hover {
	background-color: #444;
	color:#eee;
}

</style>
