use std::collections::HashMap;

pub type Value = i32;
pub type Result = std::result::Result<(), Error>;
pub type OpResult = std::result::Result<Vec<String>, Error>;
type OpFunc = fn(vec: Vec<String>) -> OpResult;

pub struct Forth {
    stack: Vec<String>,
    token: HashMap<String, Vec<String>>,
    op: HashMap<String, OpFunc>,
    val_stack: Vec<Value>,
}

#[derive(Debug, PartialEq, Eq)]
pub enum Error {
    DivisionByZero,
    StackUnderflow,
    UnknownWord,
    InvalidWord,
}

impl Forth {
    pub fn new() -> Forth {
        let mut op: HashMap<String, OpFunc> = HashMap::new();
        op.insert("+".to_string(), op_add);
        op.insert("-".to_string(), op_sub);
        op.insert("*".to_string(), op_mul);
        op.insert("/".to_string(), op_div);
        op.insert("dup".to_string(), op_dup);
        op.insert("drop".to_string(), op_drop);
        op.insert("swap".to_string(), op_swap);
        op.insert("over".to_string(), op_over);
        Self {
            stack: Vec::new(),
            token: HashMap::new(),
            op,
            val_stack: Vec::new(),
        }
    }

    pub fn stack(&mut self) -> &[Value] {
        self.val_stack.clear();
        for s in &self.stack {
            let num = s.parse::<Value>().expect("not a valid number");
            self.val_stack.push(num);
        }
        &self.val_stack
    }

    pub fn eval(&mut self, input: &str) -> Result {
        let input = input.split_whitespace().map(|s| s.to_lowercase()).collect::<Vec<String>>();
        if input.is_empty() {
            return Err(Error::InvalidWord);
        }

        if input[0] == ":" {
            let variable = input[1].to_string();
            let rest = input[2..input.len() - 1].to_vec();
            if rest.is_empty() {
                return Err(Error::UnknownWord);
            }
            if variable.parse::<Value>().is_ok() {
                return Err(Error::InvalidWord);
            }
            let ans = self.eval_expression(rest.clone()).unwrap_or(rest);
            self.token.insert(variable.clone(), ans);
        } else {
            let ans = self.eval_expression(input)?;
            self.stack.extend(ans);
        }
        Ok(())
    }

    // must have all the tokens known.
    fn eval_expression(&mut self, vec: Vec<String>) -> OpResult {
        let mut stack = Vec::<String>::new();
        for s in vec {
            if s.parse::<Value>().is_ok() {
                stack.push(s);
                continue;
            }

            if self.token.contains_key(&s) {
                let val = self.token.get(&s).unwrap().to_owned();
                stack.extend(val);
                stack = self.eval_expression(stack)?;
                continue;
            }

            if self.op.contains_key(&s) {
                stack = self.op[&s](stack)?;
                continue;
            }
            return Err(Error::UnknownWord);
        }
        Ok(stack)
    }
}

fn op_dup(mut vec: Vec<String>) -> OpResult {
    if vec.is_empty() {
        return Err(Error::StackUnderflow);
    }
    vec.push(vec.last().unwrap().to_owned());
    Ok(vec)
}

fn op_drop(mut vec: Vec<String>) -> OpResult {
    if vec.is_empty() {
        return Err(Error::StackUnderflow);
    }
    vec.pop();
    Ok(vec)
}

fn op_swap(mut vec: Vec<String>) -> OpResult {
    if vec.len() < 2 {
        return Err(Error::StackUnderflow);
    }
    let a = vec.pop().unwrap();
    let b = vec.pop().unwrap();
    vec.push(a);
    vec.push(b);
    Ok(vec)
}

fn op_over(mut vec: Vec<String>) -> OpResult {
    if vec.len() < 2 {
        return Err(Error::StackUnderflow);
    }
    let a = vec.pop().unwrap();
    let b = vec.pop().unwrap();
    vec.push(b.to_string());
    vec.push(a);
    vec.push(b);
    Ok(vec)
}

fn op_add(mut vec: Vec<String>) -> OpResult {
    if vec.len() < 2 {
        return Err(Error::StackUnderflow);
    }
    let (a, b) = (vec.pop().unwrap(), vec.pop().unwrap());
    let a = match a.parse::<Value>() {
        Ok(num) => num,
        Err(_) => return Err(Error::InvalidWord),
    };
    let b = match b.parse::<Value>() {
        Ok(num) => num,
        Err(_) => return Err(Error::InvalidWord),
    };
    vec.push((a + b).to_string());
    Ok(vec)
}

fn op_sub(mut vec: Vec<String>) -> OpResult {
    if vec.len() < 2 {
        return Err(Error::StackUnderflow);
    }
    let (b, a) = (vec.pop().unwrap(), vec.pop().unwrap());
    let a = match a.parse::<Value>() {
        Ok(num) => num,
        Err(_) => return Err(Error::InvalidWord),
    };
    let b = match b.parse::<Value>() {
        Ok(num) => num,
        Err(_) => return Err(Error::InvalidWord),
    };
    vec.push((a - b).to_string());
    Ok(vec)
}

fn op_mul(mut vec: Vec<String>) -> OpResult {
    if vec.len() < 2 {
        return Err(Error::StackUnderflow);
    }
    let (a, b) = (vec.pop().unwrap(), vec.pop().unwrap());
    let a = match a.parse::<Value>() {
        Ok(num) => num,
        Err(_) => return Err(Error::InvalidWord),
    };
    let b = match b.parse::<Value>() {
        Ok(num) => num,
        Err(_) => return Err(Error::InvalidWord),
    };
    vec.push((a * b).to_string());
    Ok(vec)
}

fn op_div(mut vec: Vec<String>) -> OpResult {
    if vec.len() < 2 {
        return Err(Error::StackUnderflow);
    }
    let (b, a) = (vec.pop().unwrap(), vec.pop().unwrap());
    let a = match a.parse::<Value>() {
        Ok(num) => num,
        Err(_) => return Err(Error::InvalidWord),
    };
    let b = match b.parse::<Value>() {
        Ok(num) => num,
        Err(_) => return Err(Error::InvalidWord),
    };
    if b == 0 {
        return Err(Error::DivisionByZero);
    }
    vec.push((a / b).to_string());
    Ok(vec)
}
