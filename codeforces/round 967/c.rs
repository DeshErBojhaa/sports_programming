use std::fmt::Display;
use std::io::{stdin, stdout, BufRead, BufReader, BufWriter, Read, Stdin, Stdout, Write};

struct IO<Input, Output>
where
    Input: Read,
    Output: Write,
{
    input: BufReader<Input>,
    output: BufWriter<Output>,
    buffer: Vec<String>,
}

#[allow(dead_code)]
impl<Input, Output> IO<Input, Output>
where
    Input: Read,
    Output: Write,
{
    fn new(input: Input, output: Output) -> Self {
        Self {
            input: BufReader::new(input),
            output: BufWriter::new(output),
            buffer: vec![],
        }
    }

    fn next<T: std::str::FromStr>(&mut self) -> T {
        loop {
            if let Some(token) = self.buffer.pop() {
                return token.parse().ok().expect("Failed parsing");
            }
            let mut inp = String::new();
            self.input.read_line(&mut inp).expect("Failed read");
            self.buffer = inp.split_whitespace().rev().map(String::from).collect();
        }
    }

    fn print(&mut self, value: impl Display) {
        writeln!(self, "{}", value).ok();
    }

    fn prints(&mut self, items: &[impl Display], sep: &str) {
        writeln!(
            self,
            "{}",
            items
                .iter()
                .map(|x| x.to_string())
                .collect::<Vec<_>>()
                .join(sep)
        )
        .ok();
    }
}

impl<Input, Output> Write for IO<Input, Output>
where
    Input: Read,
    Output: Write,
{
    fn write(&mut self, buf: &[u8]) -> std::io::Result<usize> {
        self.output.write(buf)
    }

    fn flush(&mut self) -> std::io::Result<()> {
        self.output.flush()
    }
}

impl Default for IO<Stdin, Stdout> {
    fn default() -> Self {
        Self::new(stdin(), stdout())
    }
}

fn solve(n: usize, io: &mut IO<Stdin, Stdout>) {
    let mut par = vec![0; n];
    let mut edges = vec![];

    for i in 1..n {
        while par[i] != i {
            let (mut a, b) = (0, i);
            loop {
                writeln!(io, "? {} {}", a + 1, b + 1).unwrap();
                io.flush().unwrap();
                let c = io.next::<usize>() - 1;
                if c == a {
                    edges.push((a + 1, b + 1));
                    break;
                }
                a = c;
            }
            par[i] = i;
        }
    }
    write!(io, "!").unwrap();
    for (a, b) in edges {
        write!(io, " {} {}", a, b).unwrap();
    }
    writeln!(io).unwrap();
    io.flush().unwrap();
}

fn main() {
    let mut io = IO::default();
    for _ in 0..io.next() {
        let n: usize = io.next();
        solve(n, &mut io);
    }
}
