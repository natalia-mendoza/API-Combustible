@function valid-radius($radius) {
    $return: ();
    @each $value in $radius {
      @if type-of($value) == number {
        $return: append($return, max($value, 0));
      } @else {
        $return: append($return, $value);
      }
    }
    @return $return;
  }
  
  // scss-docs-start border-radius-mixins
  @mixin border-radius($radius: $border-radius, $fallback-border-radius: false) {
    @if $enable-rounded {
      border-radius: valid-radius($radius);
    }
    @else if $fallback-border-radius != false {
      border-radius: $fallback-border-radius;
    }
  }
  
  @mixin border-top-radius($radius: $border-radius) {
    @if $enable-rounded {
      border-top-left-radius: valid-radius($radius);
      border-top-right-radius: valid-radius($radius);
    }
  }
  
  @mixin border-end-radius($radius: $border-radius) {
    @if $enable-rounded {
      border-top-right-radius: valid-radius($radius);
      border-bottom-right-radius: valid-radius($radius);
    }
  }
  
  @mixin border-bottom-radius($radius: $border-radius) {
    @if $enable-rounded {
      border-bottom-right-radius: valid-radius($radius);
      border-bottom-left-radius: valid-radius($radius);
    }
  }
  
  @mixin border-start-radius($radius: $border-radius) {
    @if $enable-rounded {
      border-top-left-radius: valid-radius($radius);
      border-bottom-left-radius: valid-radius($radius);
    }
  }
  
  @mixin border-top-start-radius($radius: $border-radius) {
    @if $enable-rounded {
      border-top-left-radius: valid-radius($radius);
    }
  }
  
  @mixin border-top-end-radius($radius: $border-radius) {
    @if $enable-rounded {
      border-top-right-radius: valid-radius($radius);
    }
  }
  
  @mixin border-bottom-end-radius($radius: $border-radius) {
    @if $enable-rounded {
      border-bottom-right-radius: valid-radius($radius);
    }
  }
  
  @mixin border-bottom-start-radius($radius: $border-radius) {
    @if $enable-rounded {
      border-bottom-left-radius: valid-radius($radius);
    }
  }
  // scss-docs-end border-radius-mixins
  