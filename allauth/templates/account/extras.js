/* 
     <p>
                <center>
                    {% blocktrans with site.name as site_name %}Please sign in with one
                    of your existing third party accounts. Or, <a href="{{ signup_url }}">click here</a>
                    to sign up for a {{ site_name }} account and sign in below:{% endblocktrans %}
                </center>
                <hr>
            </p>
 

<h1>{% trans "Sign In" %}</h1>
    <hr>
    <a class="btn btn-outline-light col-2" href="{% url 'account_signup' %}" type="button">Sign Up for MunchySite</a>
    <hr>


    {% get_providers as socialaccount_providers %}

    <div class="socialaccount_ballot">
        <center>




            <p>
                <center>
                    {% blocktrans with site.name as site_name %}Please sign in with a MunchySite Account or one
                    of your existing third party accounts.{% endblocktrans %}
                </center>
                <hr>
            </p>



            <!--  <div class="login-or">trans or</div> -->
            <br>
        </center>
    </div>

    {% include "socialaccount/snippets/login_extra.html" %}



    <h5>Sign in with MunchySite Account:</h5>
    <form class="login" method="POST" action="{% url 'account_login' %}">
        <br>

        {% csrf_token %}
        {{ form.as_p }}
        {% if redirect_field_value %}
        <input type="hidden" name="{{ redirect_field_name }}" value="{{ redirect_field_value }}" />
        {% endif %}

        <a class="primaryAction btn btn-outline-light col-2" role="button" href="{% url 'account_login' %}" type="submit">{% trans "Sign In" %}</a>
    </form>
        <br>
        <br>
        <a class="button secondaryAction" href="{% url 'account_reset_password' %}">{% trans "Forgot Password?" %}</a>
        <hr>
        <h5>Sign in with:</h5>
        {% if socialaccount_providers %}
        <p class="socialaccount_providers">
            {% include "socialaccount/snippets/provider_list.html" with process="login" %}
        </p>
        {% else %}
        <p>
            <center>
                {% blocktrans %}If you have not created an account yet, then please
                <a href="{{ signup_url }}">sign up</a> first.{% endblocktrans %}
            </center>
        </p>
        {% endif %}

</center>
{% endblock %}

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 */