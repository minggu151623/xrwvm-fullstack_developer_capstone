import React, { useState } from "react";

export default function Register() {
  const [form, setForm] = useState({ username: "", firstName: "", lastName: "", email: "", password: "" });

  const update = (event) => setForm({ ...form, [event.target.name]: event.target.value });

  return (
    <section className="register-page">
      <h1>Sign-up</h1>
      <form onSubmit={(event) => event.preventDefault()}>
        <input name="username" placeholder="Username" value={form.username} onChange={update} required />
        <input name="firstName" placeholder="First Name" value={form.firstName} onChange={update} required />
        <input name="lastName" placeholder="Last Name" value={form.lastName} onChange={update} required />
        <input name="email" type="email" placeholder="email" value={form.email} onChange={update} required />
        <input name="password" type="password" placeholder="Password" value={form.password} onChange={update} required />
        <button type="submit">Register</button>
      </form>
    </section>
  );
}
