<script>
	import { onMount } from 'svelte';

	let name = "";
	let email = "";

	let contactList = []

	onMount(async () => {
		const contatos = await fetch("http://localhost:3001/contacts")
		contactList = await contatos.json()
	})

	async function addContact(e){
		e.preventDefault()
		const data = { name, email }

		const contact = await fetch("http://localhost:3001/addcontacts", {
			method: "POST",
			headers: { "content-type":"application/json" },
			body: JSON.stringify(data)
		})

		contactList = [...contactList, await contact.json()]
		name = "";
		email = "";

	}

</script>

<main>
<form action="">
	<fieldset>
		<legend>Cadastro de Contatos</legend>
		<input type="text" placeholder="Nome Completo" bind:value={name}>
		<input type="email" placeholder="Seu Melhor E-mail" bind:value={email}>
		<button on:click={addContact} type="submit">Cadastrar</button>
	</fieldset>
</form>

<div class="box">

<h2>Lista de Contatos</h2>
<hr>

<table>
	<thead>
		<tr>
			<td>NOME</td>
			<td>E-MAIL</td>
		</tr>
	</thead>
	<tbody>
		{#each contactList as dados}
		<tr>
			<td>{dados.name}</td>
			<td>{dados.email}</td>
		</tr>
		{/each}
	</tbody>
</table>

</div>
</main>	

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	.box {
		width: 100%;
		margin-top: 50px;
	}

	table {
		width: 80%;
		margin: 0 auto;
		text-align: center;
	}
	
	table td {
		border: 1px solid #000;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>